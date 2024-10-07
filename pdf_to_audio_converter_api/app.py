from fastapi.responses import StreamingResponse
import pytesseract
from gtts import gTTS
from PyPDF2 import PdfReader
import os
import io
from PIL import Image

app = FastAPI()

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != 'application/pdf':
        raise HTTPException(status_code=415, detail="Unsupported file type.")
    try:
        content = await file.read()
        with open(f"temp/{file.filename}", "wb") as f:
            f.write(content)
        return {"filename": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/convert/")
async def convert_pdf_to_audio(filename: str):
    try:
        pdf_path = f"temp/{filename}"
        if not os.path.exists(pdf_path):
            raise HTTPException(status_code=404, detail="File not found.")

        # Attempt to extract text using PdfReader initially
        reader = PdfReader(pdf_path)
        text = ''
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:  # If text is extracted using PdfReader
                text += page_text + ' '
            else:  # If PdfReader fails, attempt OCR with pytesseract
                images = page.to_images()
                for image in images:
                    img = Image.open(io.BytesIO(image[1]))
                    text += pytesseract.image_to_string(img) + ' '

        audio = gTTS(text=text, lang='en')
        audio_file = f"temp/{filename.split('.')[0]}.mp3"
        audio.save(audio_file)

        return {"audio_file": audio_file}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stream/{audio_filename}")
async def stream_audio(audio_filename: str):
    audio_path = f"temp/{audio_filename}"
    if not os.path.exists(audio_path):
        raise HTTPException(status_code=404, detail="Audio file not found.")

    def iterfile():
        with open(audio_path, mode="rb") as file_like:
            yield from file_like

    return StreamingResponse(iterfile(), media_type="audio/mpeg")

# Cleanup function to remove temporary files
@app.on_event("shutdown")
def cleanup():
    folder = 'temp/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")
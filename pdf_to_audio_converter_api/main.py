from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
import PyPDF2
from gtts import gTTS
import io
import os

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="pdf_to_audio_converter_api/static"), name="static")

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != 'application/pdf':
        return {"error": "File type not supported. Please upload a PDF file."}
    
    try:
        # Read PDF file
        pdfReader = PyPDF2.PdfFileReader(file.file)
        text = ""
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            text += pageObj.extractText()
        
        # Convert text to audio
        tts = gTTS(text=text, lang='en')
        temp_filename = "temp_audio.mp3"
        with open(temp_filename, "wb") as audio_file:
            tts.write_to_fp(audio_file)
        
        def iterfile():
            with open(temp_filename, "rb") as audio:
                yield from audio
        
        response = StreamingResponse(iterfile(), media_type="audio/mpeg")
        
        # Clean up: Remove temporary file after streaming
        response.background = BackgroundTask(os.remove, temp_filename)
        return response
    except Exception as e:
        return {"error": "Failed to convert PDF to audio. " + str(e)}

@app.get("/play")
async def play_audio(file_path: str):
    try:
        # Open audio file
        def iterfile():
            with open(file_path, mode="rb") as file_like:
                yield from file_like
        
        return StreamingResponse(iterfile(), media_type="audio/mpeg")
    except Exception as e:
        return {"error": "Failed to play audio. " + str(e)}
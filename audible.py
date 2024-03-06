from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import cv2
import pyttsx3
import re
import json
import os
from typing import List

app = FastAPI()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text, filename="audible.mp3"):
    engine.save_to_file(text, filename)
    engine.runAndWait()
    return filename

def process_pdf_to_audio(pdf_file: bytes, poppler_path: str = r'path') -> str:
    images = convert_from_path(pdf_path=pdf_file, poppler_path=poppler_path)
    sent = ""
    for count, img in enumerate(images):
        img_name = f"page_{count+1}.png"
        img.save(img_name, "PNG")
        img_cv = cv2.imread(img_name)
        text = pytesseract.image_to_string(Image.open(img_name), lang='eng')
        sent += text
        os.remove(img_name)
    audio_file = talk(sent)
    return audio_file

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        audio_file = process_pdf_to_audio(contents)
        return FileResponse(path=audio_file, filename=audio_file, media_type='audio/mpeg')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
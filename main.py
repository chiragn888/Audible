# main.py

from fastapi import FastAPI, File, UploadFile
from auth import authenticate_user, get_current_user
from audible import convert_pdf_to_mp3

app = FastAPI()

@app.post("/login/")
def login(username: str, password: str):
    if authenticate_user(username, password):
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid credentials"}

@app.post("/upload/")
def upload_file(file: UploadFile = File(...), current_user: User = Depends(get_current_user)):
    mp3_file = convert_pdf_to_mp3(file)
    return {"message": "File converted to MP3", "file": mp3_file}
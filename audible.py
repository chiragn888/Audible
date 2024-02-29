from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import cv2
import os
from googletrans import Translator
from text_to_speech import speak
import pyttsx3
import re
import json
from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    speak(text, 'en', file="audible.mp3", save=True, speak=False)

@app.route('/process_pdf', methods=['POST'])
def process_pdf():
    if 'pdf' not in request.files:
        return "No file part", 400
    file = request.files['pdf']
    if file.filename == '':
        return "No selected file", 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        pdf_path = os.path.join('/tmp', filename)
        file.save(pdf_path)
        poppler_path = r'path'  # Replace with the actual path to Poppler
        images = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
        file_names = []
        for count, img in enumerate(images):
            img_name = f"/tmp/page_{count+1}.png"
            img.save(img_name, "PNG")
            file_names.append(img_name)
        sent = ""
        for file_name in file_names:
            img = cv2.imread(file_name)
            text = pytesseract.image_to_string(Image.open(file_name), lang='eng')
            sent += text
        with open('/tmp/audible.txt', 'w', encoding='utf-8') as f:
            print(sent, file=f)
        talk(sent)
        return "Processing complete. Use /get_audio to retrieve the MP3 file.", 200

@app.route('/get_audio', methods=['GET'])
def get_audio():
    return send_from_directory('/tmp', 'audible.mp3')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'pdf'}

if __name__ == '__main__':
    app.run(debug=True)
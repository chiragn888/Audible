from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import cv2
import os
from text_to_speech import speak
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def convert_pdf_to_audio(pdf_path, poppler_path=r'path'):
    images = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
    file_names = []
    for count, img in enumerate(images):
        img_name = f"page_{count+1}.png"
        img.save(img_name, "PNG")
        file_names.append(img_name)

    full_text = ""
    for file in file_names:
        img = cv2.imread(file)
        text = pytesseract.image_to_string(Image.open(file), lang='eng')
        full_text += text
        os.remove(file)  # Clean up the image file after processing

    audio_file_path = "audible.mp3"
    with open('audible.txt', 'w', encoding='utf-8') as f:
        f.write(full_text)

    try:
        speak(full_text, 'en', file=audio_file_path, save=True, speak=False)
        return audio_file_path
    except Exception as e:
        return str(e)

# The following code is removed as per the plan to avoid standalone execution
# filename=input()
# print("speaking....")
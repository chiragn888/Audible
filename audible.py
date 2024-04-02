from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import cv2
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    speak(text, 'en', file="audible.mp3", save=True, speak=True)

# Define a new function to convert PDF to audio
def convert_pdf_to_audio(pdf_file_path):
    poppler_path = r'path'
    images = convert_from_path(pdf_path=pdf_file_path, poppler_path=poppler_path)
    file_names = []
    for count, img in enumerate(images):
        img_name = f"page_{count+1}.png"
        img.save(img_name, "PNG")
        file_names.append(img_name)

    sent = ""
    for file in file_names:
        img = cv2.imread(file)
        text = pytesseract.image_to_string(Image.open(file), lang='eng')
        sent += text

    with open('audible.txt', 'w', encoding='utf-8') as f:
        f.write(sent)

    print("speaking....")
    talk(sent)
    
    # Return the path to the generated audio file
    return "audible.mp3"

# The following line is commented out to disable command line input
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import cv2
import pyttsx3
import os
import tempfile

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def convert_pdf_to_audio(pdf_file_path):
    # Create a temporary directory to store images
    with tempfile.TemporaryDirectory() as temp_dir:
        # Convert PDF to a list of images
        images = convert_from_path(pdf_file_path=pdf_file_path, poppler_path=r'path')
        full_text = ""

        # Process each page/image in the PDF
        for count, img in enumerate(images):
            img_name = os.path.join(temp_dir, f"page_{count+1}.png")
            img.save(img_name, "PNG")

            # Extract text from image using OCR
            img_cv = cv2.imread(img_name)
            text = pytesseract.image_to_string(Image.open(img_name), lang='eng')
            full_text += text

        # Save the extracted text to a temporary text file
        text_file_path = os.path.join(temp_dir, 'audible.txt')
        with open(text_file_path, 'w', encoding='utf-8') as f:
            f.write(full_text)

        # Generate audio from text
        audio_file_path = os.path.join(temp_dir, 'audible.mp3')
        engine.save_to_file(full_text, audio_file_path)
        engine.runAndWait()

        # Return the path to the audio file
        return audio_file_path

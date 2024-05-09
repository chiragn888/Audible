import tensorflow as tf
import pandas as pd
from pdf2image import convert_from_path
from PIL import Image
from numpy import append
import pytesseract
import cv2
from distutils.command.config import config
from googletrans import Translator
import os
from text_to_speech import speak
import pyttsx3
import re
import json

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
sent=""

def talk(text):
    speak(text,'en',file="audible.mp3",save=True, speak=True)

filename=input()
poppler_path = r'path'
pdf_path = filename
images = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
file_names=[]
for count, img in enumerate(images):
    img_name = f"page_{count+1}.png"
    img.save(img_name, "PNG")
    file_names.append(img_name)
print(file_names)

for file in file_names:
    img=cv2.imread(file)
    text=pytesseract.image_to_string(Image.open(file), lang='eng')
    sent=sent+text
with open('audible.txt', 'w', encoding='utf-8') as f:
    f.write(sent)

abcd=open("audible.txt",'r').read()
print("speaking....")
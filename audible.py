from pdf2image import convert_from_path
from PIL import Image
import cv2
import numpy as np
import pytesseract
from moviepy.editor import AudioFileClip, ColorClip, TextClip, CompositeVideoClip
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
    print(sent, file=f)

abcd=open("audible.txt",'r').read()
print("speaking....")
talk(abcd)

def create_video_with_subtitles(audio_path, subtitle_text, video_path='output_video.mp4'):
    # Load the audio file
    audio_clip = AudioFileClip(audio_path)
    # Calculate duration of the audio file
    duration = audio_clip.duration
    # Create a blank color clip as a background
    color_clip = ColorClip(size=(640, 480), color=(255, 255, 255), duration=duration)
    # Generate a subtitle clip
    subtitle_clip = TextClip(subtitle_text, fontsize=24, color='black', size=color_clip.size)
    subtitle_clip = subtitle_clip.set_position(('center', 'bottom')).set_duration(duration)
    # Composite the audio and subtitle clips
    final_video = CompositeVideoClip([color_clip, subtitle_clip], size=color_clip.size)
    final_video = final_video.set_audio(audio_clip)
    # Write the result to a file
    final_video.write_videofile(video_path, fps=24)

# Create a video with the spoken text as subtitles
create_video_with_subtitles('audible.mp3', abcd)
print("Video created with subtitles.")
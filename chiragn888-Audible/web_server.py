```python
# web_server.py

from flask import Flask, render_template, request, redirect, url_for
from audible import convert_pdf_to_audio

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Authentication logic here
    # Redirect to upload page upon successful login
    return redirect(url_for('upload'))

@app.route('/upload')
def upload_page():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Handle the POST request of the file upload
    uploaded_file = request.files['file']
    # File upload logic here
    return "File uploaded successfully"

@app.route('/convert')
def convert():
    # Call the 'convert_pdf_to_audio' function from 'audible.py'
    audio_file = convert_pdf_to_audio('uploaded_file.pdf')
    # Send the audio file back to the user
    # Audio file sending logic here
    return "Audio file sent successfully"

if __name__ == '__main__':
    app.run(debug=True)
```
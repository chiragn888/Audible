from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from audible import convert_pdf_to_audio

app = Flask(__name__)

# Serve login.html
@app.route('/')
def index():
    return render_template('login.html')

# Handle user authentication
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Add user authentication logic here
    # Example: if username == 'example' and password == 'password':
    #             return 'Login successful'
    #         else:
    #             return 'Login failed'

# Serve upload.html
@app.route('/upload')
def upload_file():
    return render_template('upload.html')

# Handle file receiving and processing
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        file.save(filename)
        convert_pdf_to_audio(filename)  # Assuming convert_pdf_to_audio is a function from audible.py
        return 'File uploaded and processed successfully'

if __name__ == '__main__':
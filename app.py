from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.utils import secure_filename
from audible import convert_pdf_to_audio
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'uploads'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'pdf', 'txt'}  # Example of allowed file types

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('upload'))
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  # Assuming there's a password field in the form
        if username == 'expected_username' and password == 'expected_password':  # Simple check for demonstration
            session['username'] = username
            return redirect(url_for('upload'))
        else:
            return 'Invalid credentials', 401
    return render_template('login.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'username' in session:
        if request.method == 'POST':
            if 'file' not in request.files:
                return 'No file part', 400
            f = request.files['file']
            if f.filename == '':
                return 'No selected file', 400
            if f and allowed_file(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return 'File uploaded successfully'
            else:
                return 'Invalid file type', 400
        return render_template('upload.html')
    else:
        return redirect(url_for('login'))

@app.route('/convert')
def convert():
    if 'username' in session:
        audio_file = convert_pdf_to_audio('uploads/example.pdf')
        return audio_file
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
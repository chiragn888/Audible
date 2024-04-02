from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from audible import convert_pdf_to_audio

app = Flask(__name__)
app.secret_key = 'supersecretkey'

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
        password = request.form['password']
        if username == 'admin' and password == 'password':
            session['username'] = username
            return redirect(url_for('upload'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'username' in session:
        if request.method == 'POST':
            file = request.files['file']
            filename = secure_filename(file.filename)
            file.save('uploads/' + filename)
            return 'File uploaded successfully'
        return render_template('upload.html')
    else:
        return redirect(url_for('login'))

@app.route('/convert')
def convert():
    if 'username' in session:
        audio_file_path = convert_pdf_to_audio('uploads/example.pdf')  # Assuming 'example.pdf' is the file to be converted
        return send_from_directory(directory='uploads', filename=audio_file_path, as_attachment=True)
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
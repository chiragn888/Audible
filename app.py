# app.py

from flask import Flask, render_template, request, send_file
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from audible import convert_pdf_to_audio

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class UploadForm(FlaskForm):
    pdf_file = FileField(validators=[FileRequired()])

@app.route('/login')
def login():
    # Render login form template
    return render_template('login.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        pdf_file = form.pdf_file.data
        filename = secure_filename(pdf_file.filename)
        pdf_file.save(f'/tmp/{filename}')
        convert_pdf_to_audio(f'/tmp/{filename}')
        return 'File uploaded and converted successfully!'
    return render_template('upload.html', form=form)

@app.route('/audio/<filename>')
def audio(filename):
    # Serve the converted audio file to the user
    return send_file(f'/path/to/converted/audio/{filename}', as_attachment=True)

if __name__ == '__main__':
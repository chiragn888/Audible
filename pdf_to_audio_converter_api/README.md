
This project provides a simple web interface and API for converting PDF documents into audio files. Users can upload a PDF file through the UI, which is then processed by the backend to extract text and convert it into an audio file using text-to-speech technology. The resulting audio can be listened to directly on the website or downloaded for offline use.

## Prerequisites

Before running the project, ensure you have the following dependencies installed:

- FastAPI: A modern, fast web framework for building APIs with Python 3.7+.
- Uvicorn: An ASGI server for running FastAPI applications.
- PyPDF2: A library for reading PDF files and extracting text.
- gTTS (Google Text-to-Speech): A library that converts text into speech.
- python-multipart: A library for handling multipart/form-data in FastAPI, which is necessary for file uploads.

These dependencies are listed in `requirements.txt` and can be installed using pip:

```
pip install -r requirements.txt
```

## Setting Up and Running the Project

To set up and run the project locally, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Start the FastAPI server:

```
uvicorn main:app --reload
```

The `--reload` flag enables auto-reload so the server will restart after code changes. This is useful during development but should be omitted in a production environment.

## Usage Instructions

1. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the UI.
2. Use the file input (`id="pdf-file"`) to select a PDF file from your computer.
3. Click the "Convert to Audio" button to upload the PDF and convert it to audio via the `/upload` endpoint.
4. After the conversion process completes, the audio player on the page will automatically update to play the generated audio file. You can listen to the audio directly in the browser or download the file for offline use by clicking the "Download" button.

## Troubleshooting

If you encounter any issues while using the application, consider the following troubleshooting steps:

- Ensure all dependencies are correctly installed by running `pip install -r requirements.txt`.
- Check that the PDF file you are trying to upload is not corrupted and is a valid PDF document.
- If the audio does not play, verify that your browser supports the audio format and that the audio file was correctly generated and returned by the server.
- For any server errors, consult the terminal output where the FastAPI server is running for error messages and stack traces that can help diagnose the issue.

For further assistance, please open an issue on the project's GitHub repository.
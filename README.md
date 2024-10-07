
Welcome to the PDF to Audio Converter application! This document provides all the necessary instructions to set up and run the application on your local machine. Follow the steps below to get started.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone the repository to your local machine or download the source code.
2. Navigate to the root directory of the project in your terminal.
3. Install the required dependencies by running:
   ```
   pip install -r pdf_to_audio_converter_api/requirements.txt
   ```

## Running the Application

To start the FastAPI server, execute the following command in the terminal from the root directory of the project:
```
uvicorn pdf_to_audio_converter_api.app:app --reload
```
The `--reload` flag enables live reloading so the server will automatically restart upon changes to the code.

## Accessing the User Interface

Once the FastAPI server is running, you can access the user interface by opening `pdf_to_audio_converter_ui/index.html` in your web browser. This file is a simple HTML page that interacts with the FastAPI backend to upload PDFs, convert them to audio, and provide options to download or listen to the audio directly.

## Application Functionality

- **Uploading PDFs**: The user interface allows you to select and upload PDF files that you wish to convert to audio.
- **Converting PDFs to Audio**: Upon uploading a PDF, the application extracts the text from the PDF and uses Google Text-to-Speech (GTTS) to convert the text into an audio file.
- **Listening to the Audio**: After conversion, you can either download the audio file or listen to it directly in the browser without downloading.

## Troubleshooting

If you encounter any issues while setting up or running the application, ensure that:
- All the required dependencies are installed correctly.
- The FastAPI server is running and accessible.
- You are opening the `index.html` file in a modern web browser that supports JavaScript and HTML5.

Thank you for using the PDF to Audio Converter application!
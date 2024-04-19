markdown
# PDF to Audio Converter

Convert Ebooks 📚 or pdf's to audio 🔉 files and listen to them hassle-free. This project utilizes Optical Character Recognition (OCR) and Text-to-Speech (TTS) technologies to transform PDF documents into audible formats. It's an ideal solution for those who prefer listening over reading, making learning and entertainment more accessible and enjoyable.

## Installation

To use this PDF to Audio Converter, you need to install several libraries. You can install them using the following pip commands:

```bash
pip install pytesseract
pip install pdf2image
pip install Pillow
pip install numpy
pip install opencv-python
pip install googletrans==4.0.0-rc1
pip install pyttsx3
```

Make sure you have the poppler utility installed on your system, as it is required by the pdf2image library for PDF processing.

## Usage

To convert your PDF files to audio, follow these steps:

1. Run the script using the command:
   ```bash
   python audible.py
   ```
2. When prompted, enter the filename of the PDF you wish to convert.

Please ensure that you set the correct path for the poppler utility in your system's environment variables, as it is necessary for the pdf2image library to function properly.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

The main aim of this project is to convert boring ebooks and other story books to audio files.
If you like to listen to stories than reading it then this is for you!

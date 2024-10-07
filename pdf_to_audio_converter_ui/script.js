
document.addEventListener("DOMContentLoaded", function() {
    const uploadForm = document.getElementById("upload-form");
    const fileInput = document.getElementById("pdf-file");
    const convertButton = document.getElementById("convert-button");
    const audioPlayer = document.getElementById("audio-player");
    const downloadLink = document.getElementById("download-link");
    const errorMessage = document.getElementById("error-message");

    // Hide elements that are not needed initially
    audioPlayer.style.display = "none";
    downloadLink.style.display = "none";
    errorMessage.style.display = "none";

    convertButton.addEventListener("click", function(e) {
        e.preventDefault();
        if (fileInput.files.length === 0) {
            displayError("Please select a PDF file to convert.");
            return;
        }

        const formData = new FormData();
        formData.append("file", fileInput.files[0]);

        fetch("/upload", {
            method: "POST",
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                throw new Error(data.error);
            }
            const audioUrl = data.audioUrl;
            const streamUrl = data.streamUrl;

            if (audioUrl) {
                downloadLink.href = audioUrl;
                downloadLink.style.display = "block";
            }

            if (streamUrl) {
                audioPlayer.src = streamUrl;
                audioPlayer.style.display = "block";
                audioPlayer.play();
            }
        })
        .catch(error => {
            displayError(`Conversion failed: ${error.message}`);
        });
    });

    function displayError(message) {
        errorMessage.textContent = message;
        errorMessage.style.display = "block";
    }
});
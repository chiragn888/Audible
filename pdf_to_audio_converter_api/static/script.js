
document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('pdf-upload-form');
    form.addEventListener('submit', async function(e) {
        e.preventDefault(); // Prevent the default form submission

        const formData = new FormData();
        const pdfFile = document.getElementById('pdf-file').files[0];
        formData.append('pdf-file', pdfFile);

        try {
            // Send the PDF to the server using Fetch API
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error(`Server responded with ${response.status}: ${response.statusText}`);
            }

            const data = await response.json();

            // Update the audio player source to play the audio
            const audioPlayer = document.getElementById('audio-player');
            audioPlayer.src = data.audio_url;
            audioPlayer.load();
            audioPlayer.play();
        } catch (error) {
            // Inform the user of any upload or conversion errors
            alert(`Failed to convert PDF to audio: ${error.message}`);
        }
    });
});
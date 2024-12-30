# LinguaScribe

LinguaScribe is a powerful transcription and translation web application built using Streamlit. It allows users to upload or record audio, transcribe it using Whisper models, and translate the transcription into various languages. The app is designed for accessibility, speed, and accuracy, providing a seamless user experience.

---

## Features

- **Audio Transcription**: Upload or record audio files and transcribe them using OpenAI Whisper models.
- **Language Translation**: Translate transcriptions into multiple languages using Google Translate.
- **Customizable Models**: Choose from Whisper model sizes (“tiny”, “base”, “small”, “medium”, and “large”) for varying speed and accuracy.
- **Manual Editing**: Edit transcriptions directly within the app before translation.
- **Real-Time Interface**: Interact with a user-friendly Streamlit interface optimized for performance.

---

## Getting Started

### Prerequisites

1. Python 3.9 or later
2. Required libraries (specified in `requirements.txt`)
3. `ffmpeg` (must be installed on the system; see instructions below)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/linguascribe.git
   cd linguascribe
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install `ffmpeg`:
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```

   *(On Windows, download the ffmpeg binary from [https://ffmpeg.org](https://ffmpeg.org) and add it to your PATH.)*

4. Run the application:
   ```bash
   streamlit run scribe.py
   ```

---

## Deployment

To deploy LinguaScribe on Streamlit Cloud:

1. Ensure your project includes the following files:
   - `requirements.txt`: Lists Python dependencies.
   - `packages.txt`: Lists system dependencies (e.g., `ffmpeg`).

2. Push your repository to a version control platform (e.g., GitHub).

3. Link your repository to Streamlit Cloud and deploy it.

---

## File Structure

```
linguascribe/
├── scribe.py           # Main application code
├── requirements.txt    # Python dependencies
├── packages.txt        # System dependencies (e.g., ffmpeg)
└── other files...      # Any other assets (images, CSS, etc.)
```

---

## Usage

1. Open the application in your browser.
2. Select an audio file to upload or record audio directly.
3. Choose a Whisper model for transcription.
4. View, edit, and translate the transcription in real time.

---

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push them:
   ```bash
   git push origin feature-name
   ```
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- **OpenAI Whisper**: For the transcription model.
- **Google Translate**: For the translation functionality.
- **Streamlit**: For the intuitive interface.

---

## Troubleshooting

- **AttributeError: module 'whisper' has no attribute 'load_model'**: Ensure `openai-whisper` is installed correctly.
- **Missing ffmpeg**: Install ffmpeg via `packages.txt` or manually on your system.

If issues persist, feel free to open an issue on the GitHub repository.


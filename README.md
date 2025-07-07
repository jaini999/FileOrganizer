# FolderOrganizer

FolderOrganizer is an AI-powered automation tool that organizes files in your Downloads folder in real time. It uses Google Gemini API to classify and sort documents, and automatically moves audio, video, and image files to their respective folders. All operations are logged for traceability.

## Features
- **Real-time Monitoring:** Watches your Downloads folder and processes new files as soon as they appear.
- **AI Document Classification:** Uses Gemini API to classify and sort documents (PDF, DOCX, TXT, RTF, MD) into appropriate folders.
- **Media Sorting:** Automatically moves audio (MP3), video (MP4), and image (JPG, PNG, GIF, etc.) files to dedicated folders.
- **Logging:** All file operations are logged to a local database for auditing.
- **Extensible Handlers:** Modular design allows easy addition of new file handlers.

## Supported File Types
- Documents: PDF, DOCX, TXT, RTF, MD
- Audio: MP3
- Video: MP4
- Images: JPG, JPEG, PNG, GIF, BMP, TIFF, WEBP

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/jaini999/FileOrganizer.git
cd FileOrganizer
```

### 2. Create a Virtual Environment (Recommended)
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root with your Gemini API key:
```
GEMINI_API_KEY=your_google_gemini_api_key_here
```

### 5. Run the Automation
```sh
python main.py
```

The script will start monitoring your Downloads folder and organize files as they appear.

## How to Stop the Automation
To stop the automation, simply press `Ctrl+C` in the terminal where the script is running. This will gracefully terminate the monitoring process.

## Notes
- **Do not share your `.env` file or API keys.**
- The automation uses [watchdog](https://pypi.org/project/watchdog/) for real-time folder monitoring.
- All logs are stored in the `db/` directory.
- You can extend the functionality by adding new handlers in the `handlers/` directory.

## License
This project is for personal use and demonstration purposes. Please add a license if you intend to distribute it.

## Structure
- `handlers/` — File type handlers
- `db/` — SQLite logger
- `utils/` — Utility modules (e.g., Gemini client) 
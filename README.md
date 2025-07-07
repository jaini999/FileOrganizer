# FolderOrganizer

A modular AI agent that monitors your Downloads folder and organizes files based on their type using Watchdog, Gemini API, and SQLite logging.

## Features
- Monitors Downloads folder in real-time
- Extracts and classifies PDF content using Gemini API
- Moves MP3s to Music and MP4s to Video
- Logs all operations in SQLite

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the agent:
   ```bash
   python main.py
   ```

## Structure
- `handlers/` — File type handlers
- `db/` — SQLite logger
- `utils/` — Utility modules (e.g., Gemini client) 
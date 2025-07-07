import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from handlers.document_handler import handle_document
from handlers.audio_handler import handle_audio
from handlers.video_handler import handle_video
from handlers.image_handler import handle_image

def dispatch_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    try:
        if ext in ['.pdf', '.docx', '.txt', '.rtf', '.md', '.markdown']:
            handle_document(file_path)
        elif ext == '.mp3':
            handle_audio(file_path)
        elif ext == '.mp4':
            handle_video(file_path)
        elif ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico']:
            handle_image(file_path)
        else:
            print(f"No handler for: {file_path}")
    except Exception as e:
        print(f"Error handling {file_path}: {e}")

class DownloadFolderHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            dispatch_file(event.src_path)

def main():
    downloads_folder = os.path.expanduser('~/Downloads')
    event_handler = DownloadFolderHandler()
    observer = Observer()
    observer.schedule(event_handler, downloads_folder, recursive=False)
    observer.start()
    print(f"Monitoring {downloads_folder} for new files...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main() 
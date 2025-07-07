import os
import shutil
from datetime import datetime
from db.logger import log_operation

def handle_video(file_path):
    """Handle video files (MP4) by moving them to Video folder"""
    try:
        # Create Video directory
        dest_dir = os.path.expanduser("~/Documents/Video")
        os.makedirs(dest_dir, exist_ok=True)
        
        # Move file
        filename = os.path.basename(file_path)
        dest_path = os.path.join(dest_dir, filename)
        
        # Handle filename conflicts
        counter = 1
        original_dest_path = dest_path
        while os.path.exists(dest_path):
            name, ext = os.path.splitext(original_dest_path)
            dest_path = f"{name}_{counter}{ext}"
            counter += 1
        
        shutil.move(file_path, dest_path)
        
        # Log the operation
        log_data = {
            'file_name': filename,
            'original_path': file_path,
            'new_path': dest_path,
            'file_type': 'video',
            'classified_as': 'Video',
            'timestamp': datetime.now().isoformat(),
            'status': 'success',
            'error_message': None
        }
        log_operation(**log_data)
        
        print(f"Video file '{filename}' moved to {dest_path}")
        return log_data
        
    except Exception as e:
        error_msg = f"Error processing video file {file_path}: {str(e)}"
        print(error_msg)
        
        # Log the error
        log_data = {
            'file_name': os.path.basename(file_path),
            'original_path': file_path,
            'new_path': None,
            'file_type': 'video',
            'classified_as': 'error',
            'timestamp': datetime.now().isoformat(),
            'status': 'error',
            'error_message': str(e)
        }
        log_operation(**log_data)
        
        return log_data 
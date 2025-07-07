import os
import shutil
from datetime import datetime
from db.logger import log_operation
from utils.gemini_client import classify_text
from pdfminer.high_level import extract_text

def extract_pdf_text(file_path):
    try:
        return extract_text(file_path) or ""
    except Exception as e:
        # Optionally log or print the error here
        return ""

def handle_pdf(file_path):
    file_name = os.path.basename(file_path)
    original_path = file_path
    file_type = 'pdf'
    classified_as = None
    new_path = None
    status = 'success'
    error_message = None
    timestamp = datetime.now().isoformat()
    try:
        # 1. Extract text from PDF using pdfminer.six
        text = extract_pdf_text(file_path)
        # 2. Classify text using Gemini API
        classified_as = classify_text(text)
        # 3. Determine destination folder
        home = os.path.expanduser('~')
        dest_dir = os.path.join(home, 'Documents', classified_as)
        os.makedirs(dest_dir, exist_ok=True)
        new_path = os.path.join(dest_dir, file_name)
        # 4. Move the file
        shutil.move(file_path, new_path)
    except Exception as e:
        status = 'error'
        error_message = str(e)
        new_path = None
    # 5. Log the operation
    log_operation(
        file_name=file_name,
        original_path=original_path,
        new_path=new_path,
        file_type=file_type,
        classified_as=classified_as,
        timestamp=timestamp,
        status=status,
        error_message=error_message
    )
    return {
        'file_name': file_name,
        'original_path': original_path,
        'new_path': new_path,
        'file_type': file_type,
        'classified_as': classified_as,
        'timestamp': timestamp,
        'status': status,
        'error_message': error_message
    } 
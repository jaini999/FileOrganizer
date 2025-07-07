import os
import shutil
from datetime import datetime
from utils.gemini_client import classify_text
from db.logger import log_operation

def extract_text_from_document(file_path):
    """Extract text from various document formats for classification"""
    try:
        ext = os.path.splitext(file_path)[1].lower()
        
        if ext == '.pdf':
            # Use existing PDF text extraction
            from pdfminer.high_level import extract_text
            return extract_text(file_path)
        
        elif ext == '.txt':
            # Simple text file
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        
        elif ext == '.docx':
            # Word documents
            try:
                from docx import Document
                doc = Document(file_path)
                return ' '.join([paragraph.text for paragraph in doc.paragraphs])
            except ImportError:
                return f"Word document: {os.path.basename(file_path)} (docx library not installed)"
        
        elif ext == '.rtf':
            # Rich Text Format
            try:
                import striprtf
                from striprtf.striprtf import rtf_to_text
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    rtf_content = f.read()
                return rtf_to_text(rtf_content)
            except ImportError:
                return f"RTF document: {os.path.basename(file_path)} (striprtf library not installed)"
        
        elif ext in ['.md', '.markdown']:
            # Markdown files
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        
        else:
            # For other formats, return basic info
            return f"Document: {os.path.basename(file_path)}"
            
    except Exception as e:
        return f"Document: {os.path.basename(file_path)} (extraction failed: {str(e)})"

def handle_document(file_path):
    """Handle document files by extracting text, classifying with AI, and organizing them"""
    try:
        # Extract text for classification
        text_content = extract_text_from_document(file_path)
        
        # Classify using Gemini
        category = classify_text(text_content)
        
        # Create destination directory
        dest_dir = os.path.expanduser(f"~/Documents/{category}")
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
            'file_type': 'document',
            'classified_as': category,
            'timestamp': datetime.now().isoformat(),
            'status': 'success',
            'error_message': None
        }
        log_operation(**log_data)
        
        print(f"Document '{filename}' classified as '{category}' and moved to {dest_path}")
        return log_data
        
    except Exception as e:
        error_msg = f"Error processing document {file_path}: {str(e)}"
        print(error_msg)
        
        # Log the error
        log_data = {
            'file_name': os.path.basename(file_path),
            'original_path': file_path,
            'new_path': None,
            'file_type': 'document',
            'classified_as': 'error',
            'timestamp': datetime.now().isoformat(),
            'status': 'error',
            'error_message': str(e)
        }
        log_operation(**log_data)
        
        return log_data 
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from handlers.pdf_handler import handle_pdf

if __name__ == "__main__":
    # Replace with a real PDF path for actual testing
    test_pdf_path = "/Users/rishabhjaini/Downloads/Networking_Basic.pdf"
    result = handle_pdf(test_pdf_path)
    print(result) 
from handlers.document_handler import handle_document

# Test with different document formats
test_files = [
    "/Users/rishabhjaini/Downloads/sample.pdf",
    "/Users/rishabhjaini/Downloads/sample.docx", 
    "/Users/rishabhjaini/Downloads/sample.txt",
    "/Users/rishabhjaini/Downloads/sample.md"
]

for file_path in test_files:
    print(f"\nTesting: {file_path}")
    try:
        result = handle_document(file_path)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}") 
from logger import log_operation

if __name__ == "__main__":
    log_operation(
        file_name="example.pdf",
        original_path="/Users/youruser/Downloads/example.pdf",
        new_path="/Users/youruser/Documents/Finance/example.pdf",
        file_type="pdf",
        classified_as="Finance",
        status="success",
        error_message=None
    )
    print("Test log entry inserted successfully.") 
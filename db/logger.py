import sqlite3
import os
from datetime import datetime

def get_db_path():
    # Store the database in the db/ directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, 'file_operations.db')

def init_db():
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS file_operations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT,
            original_path TEXT,
            new_path TEXT,
            file_type TEXT,
            classified_as TEXT,
            timestamp TEXT,
            status TEXT,
            error_message TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Call init_db on import
init_db()

def log_operation(file_name, original_path, new_path, file_type, classified_as, timestamp=None, status=None, error_message=None):
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    if timestamp is None:
        timestamp = datetime.now().isoformat()
    c.execute('''
        INSERT INTO file_operations (file_name, original_path, new_path, file_type, classified_as, timestamp, status, error_message)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (file_name, original_path, new_path, file_type, classified_as, timestamp, status, error_message))
    conn.commit()
    conn.close() 
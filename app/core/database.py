"""
AADHINI ERP Enterprise
Database Manager
"""

import sqlite3
from pathlib import Path

from app.core.config import Config


class DatabaseManager:
    """Handles SQLite database connection"""

    def __init__(self):
        # Create database folder if it doesn't exist
        Path(Config.DATABASE_DIR).mkdir(parents=True, exist_ok=True)

        self.db_path = Config.DATABASE_FILE

    def get_connection(self):
        """Return SQLite connection"""
        return sqlite3.connect(self.db_path)

    def initialize_database(self):
        """Create required tables"""

        conn = self.get_connection()
        cursor = conn.cursor()

        # Company Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS company (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT NOT NULL,
                gstin TEXT,
                mobile TEXT,
                email TEXT,
                address TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()
        conn.close()

        print("Database initialized successfully.")
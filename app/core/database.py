"""
AADHINI ERP Enterprise
Database Manager
"""

import sqlite3
from pathlib import Path


DB_PATH = Path("database/aadhini.db")


class DatabaseManager:

    def connect(self):
        return sqlite3.connect(DB_PATH)

    def initialize_database(self):
        self.create_company_table()

    def create_company_table(self):

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS company (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            company_name TEXT NOT NULL,
            company_code TEXT,

            gstin TEXT,
            pan TEXT,

            phone TEXT,
            mobile TEXT,

            email TEXT,
            website TEXT,

            contact_person TEXT,

            address1 TEXT,
            address2 TEXT,

            city TEXT,
            district TEXT,
            state TEXT,
            country TEXT DEFAULT 'India',

            pincode TEXT,

            status TEXT DEFAULT 'Active',

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()
        conn.close()
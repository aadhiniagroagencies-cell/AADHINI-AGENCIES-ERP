"""
AADHINI ERP Enterprise
Branch Database
"""

from app.core.database import DatabaseManager


class BranchDatabase:

    def __init__(self):
        self.db = DatabaseManager()

    def create_table(self):

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS branch
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                branch_code TEXT NOT NULL UNIQUE,

                branch_name TEXT NOT NULL,

                gstin TEXT,

                phone TEXT,

                email TEXT,

                address1 TEXT,

                status TEXT DEFAULT 'Active',

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()
        conn.close()
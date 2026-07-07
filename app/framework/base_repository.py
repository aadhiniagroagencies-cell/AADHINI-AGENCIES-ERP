"""
AADHINI ERP Enterprise
Base Repository

Reusable database repository for all modules.
"""

from app.core.database import DatabaseManager


class BaseRepository:

    def __init__(self, table_name):
        self.db = DatabaseManager()
        self.table_name = table_name

    # ---------------------------------------------------------
    # Connection
    # ---------------------------------------------------------

    def get_connection(self):
        return self.db.connect()

    # ---------------------------------------------------------
    # Execute INSERT / UPDATE / DELETE
    # ---------------------------------------------------------

    def execute(self, query, params=()):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, params)

        conn.commit()

        conn.close()

    # ---------------------------------------------------------
    # Fetch One
    # ---------------------------------------------------------

    def fetch_one(self, query, params=()):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, params)

        row = cursor.fetchone()

        conn.close()

        return row

    # ---------------------------------------------------------
    # Fetch All
    # ---------------------------------------------------------

    def fetch_all(self, query, params=()):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, params)

        rows = cursor.fetchall()

        conn.close()

        return rows

    # ---------------------------------------------------------
    # Generic Delete
    # ---------------------------------------------------------

    def delete_by_id(self, record_id):

        query = f"""
            DELETE FROM {self.table_name}
            WHERE id = ?
        """

        self.execute(query, (record_id,))

    # ---------------------------------------------------------
    # Generic Get By ID
    # ---------------------------------------------------------

    def get_by_id(self, record_id):

        query = f"""
            SELECT *
            FROM {self.table_name}
            WHERE id = ?
        """

        return self.fetch_one(query, (record_id,))

    # ---------------------------------------------------------
    # Generic Get All
    # ---------------------------------------------------------

    def get_all(self):

        query = f"""
            SELECT *
            FROM {self.table_name}
            ORDER BY id DESC
        """

        return self.fetch_all(query)

    # ---------------------------------------------------------
    # Generic Count
    # ---------------------------------------------------------

    def count(self):

        query = f"""
            SELECT COUNT(*)
            FROM {self.table_name}
        """

        row = self.fetch_one(query)

        return row[0] if row else 0
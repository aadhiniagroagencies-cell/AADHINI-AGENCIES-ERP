"""
AADHINI ERP Enterprise
Company Repository
"""

from app.core.database import Database


class CompanyRepository:

    def __init__(self):
        self.db = Database()

    def save_company(
        self,
        company_name,
        gstin,
        phone,
        email,
        website,
        address
    ):

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO company
            (
                company_name,
                gstin,
                phone,
                email,
                website,
                address
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                company_name,
                gstin,
                phone,
                email,
                website,
                address
            )
        )

        conn.commit()
        conn.close()

    def get_all_companies(self):

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM company
            ORDER BY id DESC
            """
        )

        rows = cursor.fetchall()

        conn.close()

        return rows
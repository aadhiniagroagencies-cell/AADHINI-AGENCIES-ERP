"""
AADHINI ERP Enterprise
Company Repository
"""

from app.core.database import DatabaseManager


class CompanyRepository:

    def __init__(self):
        self.db = DatabaseManager()

    # ---------------------------------------------------------
    # CREATE
    # ---------------------------------------------------------

    def save_company(
        self,
        company_name,
        company_code,
        gstin,
        phone,
        email,
        website,
        address1
    ):

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO company
            (
                company_name,
                company_code,
                gstin,
                phone,
                email,
                website,
                address1
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            company_name,
            company_code,
            gstin,
            phone,
            email,
            website,
            address1
        ))

        conn.commit()
        conn.close()

    # ---------------------------------------------------------
    # READ
    # ---------------------------------------------------------

    def get_all_companies(self):

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                company_name,
                company_code,
                gstin,
                phone,
                email,
                website,
                address1
            FROM company
            ORDER BY company_name
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows

    def get_company(self, company_id):

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                company_name,
                company_code,
                gstin,
                phone,
                email,
                website,
                address1
            FROM company
            WHERE id=?
        """, (company_id,))

        row = cursor.fetchone()

        conn.close()

        return row

    def search_companies(self, keyword):

        conn = self.db.connect()
        cursor = conn.cursor()

        search = f"%{keyword}%"

        cursor.execute("""
            SELECT
                id,
                company_name,
                company_code,
                gstin,
                phone,
                email,
                website,
                address1
            FROM company
            WHERE
                company_name LIKE ?
                OR company_code LIKE ?
                OR gstin LIKE ?
                OR phone LIKE ?
            ORDER BY company_name
        """, (
            search,
            search,
            search,
            search
        ))

        rows = cursor.fetchall()

        conn.close()

        return rows

    # ---------------------------------------------------------
    # UPDATE
    # ---------------------------------------------------------

    def update_company(
        self,
        company_id,
        company_name,
        company_code,
        gstin,
        phone,
        email,
        website,
        address1
    ):

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE company
            SET
                company_name=?,
                company_code=?,
                gstin=?,
                phone=?,
                email=?,
                website=?,
                address1=?
            WHERE id=?
        """, (
            company_name,
            company_code,
            gstin,
            phone,
            email,
            website,
            address1,
            company_id
        ))

        conn.commit()
        conn.close()

    # ---------------------------------------------------------
    # DELETE
    # ---------------------------------------------------------

    def delete_company(self, company_id):

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM company WHERE id=?",
            (company_id,)
        )

        conn.commit()
        conn.close()

    # ---------------------------------------------------------
    # DASHBOARD
    # ---------------------------------------------------------

    def get_company_count(self):

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM company"
        )

        count = cursor.fetchone()[0]

        conn.close()

        return count
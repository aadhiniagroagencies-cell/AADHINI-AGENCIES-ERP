"""
Company Repository
AADHINI ERP Enterprise
"""

import sqlite3

from app.core.config import Config


class CompanyRepository:

    def __init__(self):
        self.create_table()

    def get_connection(self):
        return sqlite3.connect(Config.DATABASE_FILE)

    def create_table(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS company (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            company_name TEXT NOT NULL,
            company_code TEXT,

            owner_name TEXT,

            mobile TEXT,
            phone TEXT,

            email TEXT,
            website TEXT,

            gst_number TEXT,
            pan_number TEXT,

            address1 TEXT,
            address2 TEXT,

            city TEXT,
            district TEXT,
            state TEXT,
            country TEXT,

            pincode TEXT,

            financial_year TEXT,

            logo_path TEXT,

            status TEXT,

            created_at TEXT,
            updated_at TEXT
        )
        """)

        conn.commit()
        conn.close()

    def add_company(self, company):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO company(

            company_name,
            company_code,
            owner_name,
            mobile,
            phone,
            email,
            website,
            gst_number,
            pan_number,
            address1,
            address2,
            city,
            district,
            state,
            country,
            pincode,
            financial_year,
            logo_path,
            status,
            created_at,
            updated_at

        )

        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,

        (

            company.company_name,
            company.company_code,
            company.owner_name,
            company.mobile,
            company.phone,
            company.email,
            company.website,
            company.gst_number,
            company.pan_number,
            company.address1,
            company.address2,
            company.city,
            company.district,
            company.state,
            company.country,
            company.pincode,
            company.financial_year,
            company.logo_path,
            company.status,
            company.created_at,
            company.updated_at

        ))

        conn.commit()
        conn.close()

    def get_all_companies(self):

        conn = self.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM company
        ORDER BY company_name
        """)

        data = cursor.fetchall()

        conn.close()

        return data

    def delete_company(self, company_id):

        conn = self.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM company WHERE id=?",
            (company_id,)
        )

        conn.commit()

        conn.close()
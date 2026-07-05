import sqlite3

DB_NAME = "database/aadhini.db"


def connect():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT,
        name TEXT,
        brand TEXT,
        category TEXT,
        unit TEXT,
        purchase REAL,
        selling REAL,
        gst REAL
    )
    """)

    conn.commit()
    conn.close()


def add_product(code, name, brand, category,
                unit, purchase, selling, gst):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO products
        (
            code,
            name,
            brand,
            category,
            unit,
            purchase,
            selling,
            gst
        )
        VALUES(?,?,?,?,?,?,?,?)
    """,
    (
        code,
        name,
        brand,
        category,
        unit,
        purchase,
        selling,
        gst
    ))

    conn.commit()
    conn.close()


def get_products():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            code,
            name,
            brand,
            category,
            unit,
            purchase,
            selling,
            gst
        FROM products
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


connect()
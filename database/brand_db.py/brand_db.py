import sqlite3

DB_NAME = "database/aadhini.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_brand_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS brands(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand_name TEXT UNIQUE NOT NULL,
            status TEXT NOT NULL DEFAULT 'Active'
        )
    """)

    conn.commit()
    conn.close()


def add_brand(brand_name, status="Active"):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO brands(brand_name,status) VALUES(?,?)",
            (brand_name, status)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def get_brands():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id,
               brand_name,
               status
        FROM brands
        ORDER BY brand_name
    """)

    rows = cur.fetchall()

    conn.close()

    return rows


def update_brand(brand_id, brand_name, status):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE brands
        SET brand_name=?,
            status=?
        WHERE id=?
    """, (brand_name, status, brand_id))

    conn.commit()
    conn.close()


def delete_brand(brand_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM brands WHERE id=?",
        (brand_id,)
    )

    conn.commit()
    conn.close()


def brand_exists(name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id FROM brands WHERE brand_name=?",
        (name,)
    )

    row = cur.fetchone()

    conn.close()

    return row is not None


create_brand_table()
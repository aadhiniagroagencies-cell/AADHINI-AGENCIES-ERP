import sqlite3

DB_NAME = "database/aadhini.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_hsn_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS hsn_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hsn_code TEXT UNIQUE NOT NULL,
            description TEXT,
            gst_rate REAL NOT NULL,
            status TEXT NOT NULL DEFAULT 'Active'
        )
    """)

    conn.commit()
    conn.close()


def add_hsn(hsn_code, description, gst_rate, status="Active"):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            INSERT INTO hsn_codes
            (hsn_code, description, gst_rate, status)
            VALUES (?, ?, ?, ?)
        """, (hsn_code, description, gst_rate, status))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def get_hsn_codes():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            id,
            hsn_code,
            description,
            gst_rate,
            status
        FROM hsn_codes
        ORDER BY hsn_code
    """)

    rows = cur.fetchall()
    conn.close()

    return rows


def update_hsn(hsn_id, hsn_code, description, gst_rate, status):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE hsn_codes
        SET
            hsn_code=?,
            description=?,
            gst_rate=?,
            status=?
        WHERE id=?
    """, (
        hsn_code,
        description,
        gst_rate,
        status,
        hsn_id
    ))

    conn.commit()
    conn.close()


def delete_hsn(hsn_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM hsn_codes WHERE id=?",
        (hsn_id,)
    )

    conn.commit()
    conn.close()


def hsn_exists(hsn_code):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id FROM hsn_codes WHERE hsn_code=?",
        (hsn_code,)
    )

    row = cur.fetchone()
    conn.close()

    return row is not None


create_hsn_table()
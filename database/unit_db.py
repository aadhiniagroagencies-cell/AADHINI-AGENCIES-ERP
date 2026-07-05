import sqlite3

DB_NAME = "database/aadhini.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_unit_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS units (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            unit_name TEXT UNIQUE NOT NULL,
            status TEXT NOT NULL DEFAULT 'Active'
        )
    """)

    conn.commit()
    conn.close()


def add_unit(unit_name, status="Active"):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO units(unit_name, status) VALUES (?, ?)",
            (unit_name, status)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def get_units():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id,
               unit_name,
               status
        FROM units
        ORDER BY unit_name
    """)

    rows = cur.fetchall()
    conn.close()

    return rows


def update_unit(unit_id, unit_name, status):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE units
        SET unit_name=?,
            status=?
        WHERE id=?
    """, (unit_name, status, unit_id))

    conn.commit()
    conn.close()


def delete_unit(unit_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM units WHERE id=?",
        (unit_id,)
    )

    conn.commit()
    conn.close()


def unit_exists(name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id FROM units WHERE unit_name=?",
        (name,)
    )

    row = cur.fetchone()
    conn.close()

    return row is not None


create_unit_table()
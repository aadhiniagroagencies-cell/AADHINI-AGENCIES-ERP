import sqlite3

DB_NAME = "database/aadhini.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_category_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT UNIQUE NOT NULL,
            status TEXT NOT NULL DEFAULT 'Active'
        )
    """)

    conn.commit()
    conn.close()


def add_category(category_name, status="Active"):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO categories(category_name,status) VALUES(?,?)",
            (category_name, status)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def get_categories():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id,
               category_name,
               status
        FROM categories
        ORDER BY category_name
    """)

    rows = cur.fetchall()

    conn.close()

    return rows


def update_category(category_id, category_name, status):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE categories
        SET category_name=?,
            status=?
        WHERE id=?
    """, (category_name, status, category_id))

    conn.commit()
    conn.close()


def delete_category(category_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM categories WHERE id=?",
        (category_id,)
    )

    conn.commit()
    conn.close()


def category_exists(name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id FROM categories WHERE category_name=?",
        (name,)
    )

    row = cur.fetchone()

    conn.close()

    return row is not None


create_category_table()
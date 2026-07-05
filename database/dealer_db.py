import sqlite3

DB_NAME = "database/aadhini.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_dealer_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS dealers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dealer_name TEXT NOT NULL,
            contact_person TEXT,
            mobile TEXT,
            email TEXT,
            gstin TEXT,
            address TEXT,
            city TEXT,
            state TEXT,
            pincode TEXT,
            status TEXT NOT NULL DEFAULT 'Active'
        )
    """)

    conn.commit()
    conn.close()


def add_dealer(
    dealer_name,
    contact_person,
    mobile,
    email,
    gstin,
    address,
    city,
    state,
    pincode,
    status="Active"
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO dealers
        (
            dealer_name,
            contact_person,
            mobile,
            email,
            gstin,
            address,
            city,
            state,
            pincode,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        dealer_name,
        contact_person,
        mobile,
        email,
        gstin,
        address,
        city,
        state,
        pincode,
        status
    ))

    conn.commit()
    conn.close()


def get_dealers():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            id,
            dealer_name,
            mobile,
            city,
            gstin,
            status
        FROM dealers
        ORDER BY dealer_name
    """)

    rows = cur.fetchall()
    conn.close()

    return rows


def create_default_data():
    pass


create_dealer_table()
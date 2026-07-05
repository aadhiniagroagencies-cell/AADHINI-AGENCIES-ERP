import sqlite3

DB_NAME = "database/aadhini.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_customer_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
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


def add_customer(
    customer_name,
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
        INSERT INTO customers
        (
            customer_name,
            mobile,
            email,
            gstin,
            address,
            city,
            state,
            pincode,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        customer_name,
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


def get_customers():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            id,
            customer_name,
            mobile,
            city,
            gstin,
            status
        FROM customers
        ORDER BY customer_name
    """)

    rows = cur.fetchall()
    conn.close()

    return rows


def update_customer(
    customer_id,
    customer_name,
    mobile,
    email,
    gstin,
    address,
    city,
    state,
    pincode,
    status
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE customers
        SET
            customer_name=?,
            mobile=?,
            email=?,
            gstin=?,
            address=?,
            city=?,
            state=?,
            pincode=?,
            status=?
        WHERE id=?
    """, (
        customer_name,
        mobile,
        email,
        gstin,
        address,
        city,
        state,
        pincode,
        status,
        customer_id
    ))

    conn.commit()
    conn.close()


def delete_customer(customer_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM customers WHERE id=?",
        (customer_id,)
    )

    conn.commit()
    conn.close()


create_customer_table()
import sqlite3
import os

# Database file path
DB_NAME = os.path.join(os.path.dirname(__file__), "aadhini.db")


def get_connection():
    """Return SQLite connection."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    """Create all required ERP master tables."""

    conn = get_connection()
    cursor = conn.cursor()

    # ===============================
    # BRAND MASTER
    # ===============================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS brands (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand_name TEXT UNIQUE NOT NULL,
        status INTEGER DEFAULT 1
    )
    """)

    # ===============================
    # CATEGORY MASTER
    # ===============================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT UNIQUE NOT NULL,
        status INTEGER DEFAULT 1
    )
    """)

    # ===============================
    # UNIT MASTER
    # ===============================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS units (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        unit_name TEXT UNIQUE NOT NULL,
        status INTEGER DEFAULT 1
    )
    """)

    # ===============================
    # HSN MASTER
    # ===============================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hsn_master (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hsn_code TEXT UNIQUE NOT NULL,
        description TEXT,
        gst_percent REAL DEFAULT 18
    )
    """)

    # ===============================
    # PRODUCT MASTER
    # ===============================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_code TEXT UNIQUE,
        product_name TEXT NOT NULL,
        brand_id INTEGER,
        category_id INTEGER,
        unit_id INTEGER,
        hsn_id INTEGER,
        gst_percent REAL,
        purchase_price REAL DEFAULT 0,
        selling_price REAL DEFAULT 0,
        mrp REAL DEFAULT 0,
        opening_stock REAL DEFAULT 0,
        reorder_level REAL DEFAULT 0,
        barcode TEXT,
        description TEXT,
        status INTEGER DEFAULT 1
    )
    """)

    conn.commit()
    conn.close()
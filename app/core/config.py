"""
AADHINI ERP Enterprise
Configuration Manager
"""

from pathlib import Path


class Config:
    """Application Configuration"""

    # --------------------------------------------------
    # Application Information
    # --------------------------------------------------
    APP_NAME = "AADHINI ERP Enterprise"
    VERSION = "0.1.0"
    COMPANY = "Aadhini Agencies"

    # --------------------------------------------------
    # Base Directory
    # --------------------------------------------------
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    # --------------------------------------------------
    # Folder Paths
    # --------------------------------------------------
    DATABASE_DIR = BASE_DIR / "database"
    DATABASE_FILE = DATABASE_DIR / "aadhini.db"

    ASSETS_DIR = BASE_DIR / "assets"
    ICONS_DIR = ASSETS_DIR / "icons"
    IMAGES_DIR = ASSETS_DIR / "images"

    REPORTS_DIR = BASE_DIR / "reports"
    BACKUPS_DIR = BASE_DIR / "backups"
    LOGS_DIR = BASE_DIR / "logs"

    # --------------------------------------------------
    # Theme
    # --------------------------------------------------
    THEME = "flatly"

    # --------------------------------------------------
    # Window Settings
    # --------------------------------------------------
    WINDOW_WIDTH = 1400
    WINDOW_HEIGHT = 850

    # --------------------------------------------------
    # Future API Configuration
    # --------------------------------------------------
    API_URL = "http://localhost:8000/api"
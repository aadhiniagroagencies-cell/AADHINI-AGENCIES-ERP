"""
AADHINI ERP Enterprise
Logger Manager
"""

import logging
from pathlib import Path

from app.core.config import Config


def setup_logger():
    """Configure application logger"""

    # Create logs directory if it doesn't exist
    Path(Config.LOGS_DIR).mkdir(parents=True, exist_ok=True)

    log_file = Config.LOGS_DIR / "aadhini_erp.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger("AADHINI_ERP")

    logger.info("=" * 60)
    logger.info("AADHINI ERP Enterprise Started")
    logger.info(f"Version : {Config.VERSION}")
    logger.info("=" * 60)

    return logger
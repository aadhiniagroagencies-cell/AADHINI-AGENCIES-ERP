from app.core.logger import setup_logger
from app.core.database import DatabaseManager
from app.core.application import AadhiniERP

logger = setup_logger()
logger.info("Starting AADHINI ERP Enterprise")

db = DatabaseManager()
db.initialize_database()

app = AadhiniERP()
app.mainloop()
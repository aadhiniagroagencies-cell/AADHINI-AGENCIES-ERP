"""
Company Model
AADHINI ERP Enterprise
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Company:
    id: int = None

    company_name: str = ""
    company_code: str = ""

    owner_name: str = ""

    mobile: str = ""
    phone: str = ""

    email: str = ""
    website: str = ""

    gst_number: str = ""
    pan_number: str = ""

    address1: str = ""
    address2: str = ""

    city: str = ""
    district: str = ""
    state: str = ""
    country: str = "India"

    pincode: str = ""

    financial_year: str = ""

    logo_path: str = ""

    status: str = "Active"

    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
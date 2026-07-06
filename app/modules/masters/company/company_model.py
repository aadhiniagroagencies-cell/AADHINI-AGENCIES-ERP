from dataclasses import dataclass


@dataclass
class Company:
    id: int = None

    company_name: str = ""
    address1: str = ""
    address2: str = ""
    city: str = ""
    state: str = ""
    pincode: str = ""

    mobile: str = ""
    email: str = ""
    website: str = ""

    gstin: str = ""
    pan: str = ""

    contact_person: str = ""

    bank_name: str = ""
    account_number: str = ""
    ifsc_code: str = ""

    logo_path: str = ""

    status: str = "Active"
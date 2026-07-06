"""
AADHINI ERP Enterprise
Company Service
"""

from app.modules.masters.company.company_repository import CompanyRepository


class CompanyService:

    def __init__(self):
        self.repository = CompanyRepository()

    def save_company(
        self,
        company_name,
        gstin,
        phone,
        email,
        website,
        address
    ):

        self.repository.save_company(
            company_name,
            gstin,
            phone,
            email,
            website,
            address
        )

    def get_all_companies(self):

        return self.repository.get_all_companies()
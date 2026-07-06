"""
Company Service
AADHINI ERP Enterprise
"""

from app.modules.masters.company_repository import CompanyRepository


class CompanyService:

    def __init__(self):
        self.repository = CompanyRepository()

    def save_company(self, company):
        self.repository.add_company(company)

    def get_companies(self):
        return self.repository.get_all_companies()

    def delete_company(self, company_id):
        self.repository.delete_company(company_id)
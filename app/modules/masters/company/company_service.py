"""
AADHINI ERP Enterprise
Company Service
"""

from app.modules.masters.company.company_repository import CompanyRepository


class CompanyService:

    def __init__(self):
        self.repository = CompanyRepository()

    # ---------------------------------------------------------
    # VALIDATION
    # ---------------------------------------------------------

    def validate_company(
        self,
        company_name,
        company_code,
        gstin,
        phone,
        email,
        website,
        address1
    ):

        if not company_name.strip():
            raise ValueError("Company Name is required.")

    # ---------------------------------------------------------
    # CREATE
    # ---------------------------------------------------------

    def save_company(
        self,
        company_name,
        company_code,
        gstin,
        phone,
        email,
        website,
        address1
    ):

        self.validate_company(
            company_name,
            company_code,
            gstin,
            phone,
            email,
            website,
            address1
        )

        self.repository.save_company(
            company_name,
            company_code,
            gstin,
            phone,
            email,
            website,
            address1
        )

    # ---------------------------------------------------------
    # READ
    # ---------------------------------------------------------

    def get_all_companies(self):
        return self.repository.get_all_companies()

    def get_company(self, company_id):
        return self.repository.get_company(company_id)

    def search_companies(self, keyword):
        return self.repository.search_companies(keyword)

    # ---------------------------------------------------------
    # UPDATE
    # ---------------------------------------------------------

    def update_company(
        self,
        company_id,
        company_name,
        company_code,
        gstin,
        phone,
        email,
        website,
        address1
    ):

        self.validate_company(
            company_name,
            company_code,
            gstin,
            phone,
            email,
            website,
            address1
        )

        self.repository.update_company(
            company_id,
            company_name,
            company_code,
            gstin,
            phone,
            email,
            website,
            address1
        )

    # ---------------------------------------------------------
    # DELETE
    # ---------------------------------------------------------

    def delete_company(self, company_id):
        self.repository.delete_company(company_id)

    # ---------------------------------------------------------
    # DASHBOARD
    # ---------------------------------------------------------

    def get_company_count(self):
        return self.repository.get_company_count()


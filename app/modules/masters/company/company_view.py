"""
Company Master View
AADHINI ERP Enterprise
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from app.models.company import Company
from app.modules.masters.company_service import CompanyService


class CompanyView(ttk.Frame):

    def __init__(self, parent):

        super().__init__(parent)

        self.service = CompanyService()

        self.pack(fill=BOTH, expand=True, padx=20, pady=20)

        self.create_widgets()

    def create_widgets(self):

        title = ttk.Label(
            self,
            text="Company Master",
            font=("Segoe UI", 20, "bold")
        )

        title.pack(anchor=W, pady=(0, 20))

        form = ttk.Frame(self)
        form.pack(fill=X)

        ttk.Label(
            form,
            text="Company Name"
        ).grid(row=0, column=0, padx=5, pady=10, sticky=W)

        self.company_name = ttk.Entry(
            form,
            width=40
        )

        self.company_name.grid(
            row=0,
            column=1,
            padx=5,
            pady=10
        )

        ttk.Label(
            form,
            text="Company Code"
        ).grid(row=1, column=0, padx=5, pady=10, sticky=W)

        self.company_code = ttk.Entry(
            form,
            width=40
        )

        self.company_code.grid(
            row=1,
            column=1,
            padx=5,
            pady=10
        )

        ttk.Button(
            self,
            text="Save Company",
            bootstyle=SUCCESS,
            command=self.save_company
        ).pack(anchor=W, pady=20)

    def save_company(self):

        company = Company()

        company.company_name = self.company_name.get()
        company.company_code = self.company_code.get()

        self.service.save_company(company)

        print("Company Saved Successfully")
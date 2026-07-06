"""
AADHINI ERP Enterprise
Company Master View
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import ttk as tkttk


class CompanyView(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.pack(fill=BOTH, expand=True, padx=20, pady=20)

        self.create_widgets()

    def create_widgets(self):

        # ---------------- Title ----------------

        ttk.Label(
            self,
            text="Company Master",
            font=("Segoe UI", 22, "bold")
        ).pack(anchor="w", pady=(0, 20))

        # ---------------- Form ----------------

        form = ttk.LabelFrame(self, text="Company Information")
        form.pack(fill=X)

        # Company Name
        ttk.Label(form, text="Company Name").grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.company_name = ttk.Entry(form, width=40)
        self.company_name.grid(row=0, column=1, padx=10, pady=10)

        # Company Code
        ttk.Label(form, text="Company Code").grid(row=0, column=2, padx=10, pady=10, sticky=W)

        self.company_code = ttk.Entry(form, width=20)
        self.company_code.grid(row=0, column=3, padx=10, pady=10)

        # GSTIN
        ttk.Label(form, text="GSTIN").grid(row=1, column=0, padx=10, pady=10, sticky=W)

        self.gstin = ttk.Entry(form, width=40)
        self.gstin.grid(row=1, column=1, padx=10, pady=10)

        # Phone
        ttk.Label(form, text="Phone").grid(row=1, column=2, padx=10, pady=10, sticky=W)

        self.phone = ttk.Entry(form, width=20)
        self.phone.grid(row=1, column=3, padx=10, pady=10)

        # Email
        ttk.Label(form, text="Email").grid(row=2, column=0, padx=10, pady=10, sticky=W)

        self.email = ttk.Entry(form, width=40)
        self.email.grid(row=2, column=1, padx=10, pady=10)

        # Website
        ttk.Label(form, text="Website").grid(row=2, column=2, padx=10, pady=10, sticky=W)

        self.website = ttk.Entry(form, width=20)
        self.website.grid(row=2, column=3, padx=10, pady=10)

        # Address
        ttk.Label(form, text="Address").grid(row=3, column=0, padx=10, pady=10, sticky=NW)

        self.address = ttk.Text(form, width=60, height=4)
        self.address.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

        # ---------------- Buttons ----------------

        button_frame = ttk.Frame(self)
        button_frame.pack(fill=X, pady=15)

        ttk.Button(button_frame, text="Save", bootstyle=SUCCESS).pack(side=LEFT, padx=5)

        ttk.Button(button_frame, text="Update", bootstyle=PRIMARY).pack(side=LEFT, padx=5)

        ttk.Button(button_frame, text="Delete", bootstyle=DANGER).pack(side=LEFT, padx=5)

        ttk.Button(button_frame, text="Clear", bootstyle=WARNING).pack(side=LEFT, padx=5)

        # ---------------- Search ----------------

        search_frame = ttk.Frame(self)
        search_frame.pack(fill=X, pady=(5, 10))

        ttk.Label(search_frame, text="Search").pack(side=LEFT)

        self.search = ttk.Entry(search_frame, width=40)
        self.search.pack(side=LEFT, padx=10)

        # ---------------- Table ----------------

        columns = (
            "ID",
            "Company",
            "GSTIN",
            "Phone"
        )

        self.table = tkttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=12
        )

        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, anchor=CENTER)

        self.table.pack(fill=BOTH, expand=True)
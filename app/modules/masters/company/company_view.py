"""
AADHINI ERP Enterprise
Company Master View

NOTE:
This is a starter template generated from the available project context.
It must be adjusted if your repository/service signatures or widget APIs
change.
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

from app.modules.masters.company.company_service import CompanyService
from app.widgets.form_header import FormHeader
from app.widgets.form_buttons import FormButtons
from app.widgets.search_bar import SearchBar
from app.widgets.data_grid import DataGrid


class CompanyView(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.service = CompanyService()
        self.selected_company = None

        FormHeader(
            self,
            "Company Master",
            "Create and manage company details"
        )

        self._build_form()

        self.buttons = FormButtons(
            self,
            save_command=self.save_company,
            update_command=self.update_company,
            delete_command=self.delete_company,
            clear_command=self.clear_form
        )

        self.search = SearchBar(
            self,
            search_command=self.search_company
        )

        self.grid = DataGrid(
            self,
            (
                "ID",
                "Company",
                "Code",
                "GSTIN",
                "Phone",
                "Email",
                "Website",
                "Address"
            )
        )

        self.grid.bind_select(self.on_row_select)

        self.load_companies()

    def _build_form(self):
        frame = ttk.Labelframe(self, text="Company Details", padding=15)
        frame.pack(fill=X, padx=10, pady=10)

        labels = [
            ("Company Name", "company_name"),
            ("Company Code", "company_code"),
            ("GSTIN", "gstin"),
            ("Phone", "phone"),
            ("Email", "email"),
            ("Website", "website"),
            ("Address", "address1"),
        ]

        self.entries = {}

        for row, (label, key) in enumerate(labels):
            ttk.Label(frame, text=label).grid(row=row, column=0, sticky=W, padx=5, pady=5)

            if key == "address1":
                widget = ttk.Text(frame, height=3, width=45)
                widget.grid(row=row, column=1, sticky=W)
            else:
                widget = ttk.Entry(frame, width=45)
                widget.grid(row=row, column=1, sticky=W)

            self.entries[key] = widget

    def _value(self, key):
        w = self.entries[key]
        if isinstance(w, ttk.Text):
            return w.get("1.0", "end").strip()
        return w.get().strip()

    def _set_value(self, key, value):
        w = self.entries[key]
        if isinstance(w, ttk.Text):
            w.delete("1.0", "end")
            w.insert("1.0", value or "")
        else:
            w.delete(0, END)
            w.insert(0, value or "")

    def clear_form(self):
        self.selected_company = None
        for key in self.entries:
            self._set_value(key, "")
        self.search.clear()

    def load_companies(self):
        rows = self.service.get_all_companies()
        self.grid.load(rows)

    def save_company(self):
        try:
            self.service.save_company(
                self._value("company_name"),
                self._value("company_code"),
                self._value("gstin"),
                self._value("phone"),
                self._value("email"),
                self._value("website"),
                self._value("address1"),
            )
            messagebox.showinfo("Success", "Company saved successfully.")
            self.load_companies()
            self.clear_form()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def update_company(self):
        if self.selected_company is None:
            messagebox.showwarning("Warning", "Select a company first.")
            return

        try:
            self.service.update_company(
                self.selected_company,
                self._value("company_name"),
                self._value("company_code"),
                self._value("gstin"),
                self._value("phone"),
                self._value("email"),
                self._value("website"),
                self._value("address1"),
            )
            messagebox.showinfo("Success", "Company updated successfully.")
            self.load_companies()
            self.clear_form()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def delete_company(self):
        if self.selected_company is None:
            messagebox.showwarning("Warning", "Select a company first.")
            return

        if not messagebox.askyesno("Confirm", "Delete selected company?"):
            return

        try:
            self.service.delete_company(self.selected_company)
            self.load_companies()
            self.clear_form()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def search_company(self):
        keyword = self.search.get()
        if keyword:
            self.grid.load(self.service.search_companies(keyword))
        else:
            self.load_companies()

    def on_row_select(self, event=None):
        row = self.grid.selected_row()
        if not row:
            return

        self.selected_company = row[0]

        mapping = [
            "company_name",
            "company_code",
            "gstin",
            "phone",
            "email",
            "website",
            "address1",
        ]

        for i, field in enumerate(mapping, start=1):
            if i < len(row):
                self._set_value(field, row[i])


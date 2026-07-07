"""
AADHINI ERP Enterprise
Reusable Search Bar
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class SearchBar(ttk.Frame):

    def __init__(
        self,
        parent,
        search_command=None
    ):
        super().__init__(parent)

        self.pack(fill=X, pady=(10, 10))

        ttk.Label(
            self,
            text="🔍 Search",
            font=("Segoe UI", 10, "bold")
        ).pack(side=LEFT)

        self.search_var = ttk.StringVar()

        self.entry = ttk.Entry(
            self,
            textvariable=self.search_var,
            width=40
        )

        self.entry.pack(side=LEFT, padx=10)

        ttk.Button(
            self,
            text="Search",
            bootstyle=INFO,
            command=search_command
        ).pack(side=LEFT)

    def get(self):
        return self.search_var.get().strip()

    def clear(self):
        self.search_var.set("")
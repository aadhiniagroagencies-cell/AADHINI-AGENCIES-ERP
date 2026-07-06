"""
AADHINI ERP Enterprise
Reusable Search Box Widget
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class SearchBox(ttk.Frame):

    def __init__(self, parent, placeholder="Search..."):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)

        self.entry = ttk.Entry(
            self,
            font=("Segoe UI", 10)
        )

        self.entry.grid(row=0, column=0, sticky="ew", padx=(0, 5))

        self.entry.insert(0, placeholder)

        self.button = ttk.Button(
            self,
            text="Search",
            bootstyle="primary"
        )

        self.button.grid(row=0, column=1)
"""
AADHINI ERP Enterprise
Professional Header
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from app.widgets.search_box import SearchBox


class Header(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bootstyle="primary")

        self.configure(height=70)
        self.pack_propagate(False)

        self.build_ui()

    def build_ui(self):

        # Configure layout
        self.columnconfigure(1, weight=1)

        # ---------------- Logo / Title ----------------
        title = ttk.Label(
            self,
            text="AADHINI ERP Enterprise",
            font=("Segoe UI", 18, "bold"),
            foreground="white"
        )
        title.grid(row=0, column=0, padx=20, pady=15, sticky="w")

        # ---------------- Search ----------------
        search = SearchBox(self)
        search.grid(row=0, column=1, padx=20, sticky="ew")

        # ---------------- Right Side ----------------
        right = ttk.Frame(self, bootstyle="primary")
        right.grid(row=0, column=2, padx=20)

        ttk.Label(
            right,
            text="Branch : Head Office",
            foreground="white",
            font=("Segoe UI", 10, "bold")
        ).pack(side=LEFT, padx=10)

        ttk.Label(
            right,
            text="FY : 2026-27",
            foreground="white",
            font=("Segoe UI", 10, "bold")
        ).pack(side=LEFT, padx=10)

        ttk.Label(
            right,
            text="User : Admin",
            foreground="white",
            font=("Segoe UI", 10, "bold")
        ).pack(side=LEFT, padx=10)
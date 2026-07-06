"""
AADHINI ERP Enterprise
Content Area
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Content(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.configure(padding=20)

        self.build_ui()

    def build_ui(self):

        title = ttk.Label(
            self,
            text="Dashboard",
            font=("Segoe UI", 24, "bold")
        )

        title.pack(anchor="w", pady=(0, 20))

        welcome = ttk.Label(
            self,
            text="Welcome to AADHINI ERP Enterprise",
            font=("Segoe UI", 12)
        )

        welcome.pack(anchor="w")

        separator = ttk.Separator(self, orient="horizontal")
        separator.pack(fill=X, pady=20)

        info = ttk.Label(
            self,
            text="Dashboard widgets will be displayed here.",
            font=("Segoe UI", 11)
        )

        info.pack(anchor="w")
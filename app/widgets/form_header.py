"""
AADHINI ERP Enterprise
Reusable Form Header Widget
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class FormHeader(ttk.Frame):

    def __init__(self, parent, title, subtitle=""):
        super().__init__(parent)

        self.pack(fill=X, pady=(0, 20))

        # Title
        ttk.Label(
            self,
            text=title,
            font=("Segoe UI", 22, "bold")
        ).pack(anchor="w")

        # Subtitle
        if subtitle:

            ttk.Label(
                self,
                text=subtitle,
                font=("Segoe UI", 10),
                bootstyle="secondary"
            ).pack(anchor="w", pady=(2, 8))

        # Separator
        ttk.Separator(self).pack(fill=X, pady=(5, 0))
"""
AADHINI ERP Enterprise
Dashboard Information Card
"""

import ttkbootstrap as ttk


class InfoCard(ttk.Frame):

    def __init__(self, parent, title, value):

        super().__init__(
            parent,
            padding=15,
            bootstyle="light"
        )

        title_label = ttk.Label(
            self,
            text=title,
            font=("Segoe UI", 10)
        )

        title_label.pack(anchor="w")

        value_label = ttk.Label(
            self,
            text=value,
            font=("Segoe UI", 20, "bold")
        )

        value_label.pack(anchor="w", pady=(8, 0))
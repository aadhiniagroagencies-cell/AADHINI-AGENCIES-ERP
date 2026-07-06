"""
AADHINI ERP Enterprise
Sidebar Layout
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from app.modules.masters.company.company_view import CompanyView


class Sidebar(ttk.Frame):

    def __init__(self, parent, content):
        super().__init__(parent)

        self.content = content

        self.configure(width=220)
        self.pack_propagate(False)

        self.build_menu()

    def build_menu(self):

        # Dashboard
        ttk.Button(
            self,
            text="🏠 Dashboard",
            bootstyle="light",
            width=22,
            command=self.content.show_dashboard
        ).pack(fill=X, padx=10, pady=4)

        ttk.Separator(self).pack(fill=X, padx=10, pady=10)

        # Masters
        ttk.Label(
            self,
            text="Masters",
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", padx=15)

        ttk.Button(
            self,
            text="🏢 Company",
            bootstyle="light",
            width=22,
            command=lambda: self.content.show_view(CompanyView)
        ).pack(fill=X, padx=10, pady=4)

        ttk.Button(
            self,
            text="🏢 Branch",
            bootstyle="light",
            width=22
        ).pack(fill=X, padx=10, pady=4)

        ttk.Separator(self).pack(fill=X, padx=10, pady=10)

        menus = [
            "📦 Inventory",
            "🛒 Purchase",
            "💰 Sales",
            "🏦 Accounts",
            "📊 Reports",
            "⚙ Settings",
            "🚪 Logout"
        ]

        for menu in menus:

            ttk.Button(
                self,
                text=menu,
                bootstyle="light",
                width=22
            ).pack(fill=X, padx=10, pady=4)
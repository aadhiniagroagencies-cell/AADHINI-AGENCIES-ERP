"""
AADHINI ERP Enterprise
Sidebar Layout
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Sidebar(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.configure(width=220)

        self.pack_propagate(False)

        self.build_menu()

    def build_menu(self):

        title = ttk.Label(
            self,
            text="MENU",
            font=("Segoe UI", 14, "bold")
        )

        title.pack(pady=(20, 15))

        menus = [
            "🏠 Dashboard",
            "📁 Masters",
            "📦 Inventory",
            "🛒 Purchase",
            "💰 Sales",
            "🏦 Accounts",
            "📊 Reports",
            "⚙ Settings",
            "🚪 Logout"
        ]

        for menu in menus:

            btn = ttk.Button(
                self,
                text=menu,
                bootstyle="light",
                width=22
            )

            btn.pack(fill=X, padx=10, pady=4)
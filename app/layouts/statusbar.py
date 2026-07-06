"""
AADHINI ERP Enterprise
Status Bar
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class StatusBar(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bootstyle="secondary")

        self.configure(height=30)

        self.build_ui()

    def build_ui(self):

        status = ttk.Label(
            self,
            text="Ready",
            font=("Segoe UI", 9)
        )

        status.pack(side=LEFT, padx=10)

        version = ttk.Label(
            self,
            text="Version 0.1.0",
            font=("Segoe UI", 9)
        )

        version.pack(side=RIGHT, padx=10)
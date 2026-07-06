"""
AADHINI ERP Enterprise
Reusable Sidebar Menu Button
"""

import ttkbootstrap as ttk


class MenuButton(ttk.Button):

    def __init__(self, parent, text, command=None):

        super().__init__(
            parent,
            text=text,
            command=command,
            bootstyle="light",
            width=24
        )
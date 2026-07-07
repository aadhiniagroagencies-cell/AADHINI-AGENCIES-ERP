"""
AADHINI ERP Enterprise
Reusable Form Buttons
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class FormButtons(ttk.Frame):

    def __init__(
        self,
        parent,
        save_command=None,
        update_command=None,
        delete_command=None,
        clear_command=None
    ):
        super().__init__(parent)

        self.pack(fill=X, pady=15)

        ttk.Button(
            self,
            text="💾 Save",
            bootstyle=SUCCESS,
            width=12,
            command=save_command
        ).pack(side=LEFT, padx=5)

        ttk.Button(
            self,
            text="✏ Update",
            bootstyle=PRIMARY,
            width=12,
            command=update_command
        ).pack(side=LEFT, padx=5)

        ttk.Button(
            self,
            text="🗑 Delete",
            bootstyle=DANGER,
            width=12,
            command=delete_command
        ).pack(side=LEFT, padx=5)

        ttk.Button(
            self,
            text="🧹 Clear",
            bootstyle=WARNING,
            width=12,
            command=clear_command
        ).pack(side=LEFT, padx=5)
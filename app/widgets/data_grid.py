"""
AADHINI ERP Enterprise
Reusable Data Grid
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import ttk as tkttk


class DataGrid(ttk.Frame):

    def __init__(self, parent, columns):
        super().__init__(parent)

        self.columns = columns

        self.pack(fill=BOTH, expand=True)

        self.build_grid()

    def build_grid(self):

        container = ttk.Frame(self)
        container.pack(fill=BOTH, expand=True)

        self.tree = tkttk.Treeview(
            container,
            columns=self.columns,
            show="headings",
            height=12
        )

        for col in self.columns:

            self.tree.heading(col, text=col)

            self.tree.column(
                col,
                width=150,
                anchor=CENTER
            )

        yscroll = ttk.Scrollbar(
            container,
            orient=VERTICAL,
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=yscroll.set
        )

        self.tree.pack(
            side=LEFT,
            fill=BOTH,
            expand=True
        )

        yscroll.pack(
            side=RIGHT,
            fill=Y
        )

    # --------------------------------

    def clear(self):

        self.tree.delete(*self.tree.get_children())

    # --------------------------------

    def load(self, rows):

        self.clear()

        for row in rows:

            self.tree.insert(
                "",
                END,
                values=row
            )

    # --------------------------------

    def selected_row(self):

        selected = self.tree.focus()

        if not selected:
            return None

        return self.tree.item(selected)["values"]

    # --------------------------------

    def bind_select(self, callback):

        self.tree.bind(
            "<<TreeviewSelect>>",
            callback
        )

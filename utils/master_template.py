import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import ttk as tkttk


class MasterTemplate:

    def __init__(self, parent, title):

        self.parent = parent
        self.title = title

        self.build_ui()

    def build_ui(self):

        for widget in self.parent.winfo_children():
            widget.destroy()

        self.main = ttk.Frame(self.parent)
        self.main.pack(fill=BOTH, expand=True, padx=20, pady=20)

        ttk.Label(
            self.main,
            text=self.title,
            font=("Segoe UI", 20, "bold")
        ).pack(anchor=W, pady=(0, 20))

        self.info_frame = ttk.LabelFrame(
            self.main,
            text="Information"
        )
        self.info_frame.pack(fill=X)

        self.button_frame = ttk.Frame(self.main)
        self.button_frame.pack(fill=X, pady=15)

        ttk.Button(
            self.button_frame,
            text="New",
            width=12
        ).pack(side=LEFT, padx=5)

        ttk.Button(
            self.button_frame,
            text="Save",
            width=12
        ).pack(side=LEFT, padx=5)

        ttk.Button(
            self.button_frame,
            text="Update",
            width=12
        ).pack(side=LEFT, padx=5)

        ttk.Button(
            self.button_frame,
            text="Delete",
            width=12
        ).pack(side=LEFT, padx=5)

        ttk.Button(
            self.button_frame,
            text="Clear",
            width=12
        ).pack(side=LEFT, padx=5)

        self.search_frame = ttk.LabelFrame(
            self.main,
            text="Search"
        )
        self.search_frame.pack(fill=X, pady=10)

        ttk.Entry(
            self.search_frame,
            width=40
        ).pack(side=LEFT, padx=10, pady=10)

        columns = ("ID", "Name", "Status")

        self.tree = tkttk.Treeview(
            self.main,
            columns=columns,
            show="headings",
            height=12
        )

        for col in columns:
            self.tree.heading(col, text=col)

        self.tree.column("ID", width=80, anchor=CENTER)
        self.tree.column("Name", width=350)
        self.tree.column("Status", width=120, anchor=CENTER)

        self.tree.pack(fill=BOTH, expand=True)

        ttk.Label(
            self.main,
            text="Ready"
        ).pack(anchor=W, pady=10)
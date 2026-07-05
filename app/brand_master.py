import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import ttk as tkttk
from tkinter import messagebox

from database.brand_db import (
    add_brand,
    get_brands,
    brand_exists,
)


def show_brand_master(parent):

    for widget in parent.winfo_children():
        widget.destroy()

    selected_id = None

    main = ttk.Frame(parent)
    main.pack(fill=BOTH, expand=True, padx=20, pady=20)

    ttk.Label(
        main,
        text="BRAND MASTER",
        font=("Segoe UI", 20, "bold")
    ).pack(anchor=W, pady=(0, 20))

    info = ttk.LabelFrame(main, text="Brand Information")
    info.pack(fill=X)

    ttk.Label(
        info,
        text="Brand Name"
    ).grid(row=0, column=0, padx=10, pady=10, sticky=W)

    txt_brand = ttk.Entry(info, width=40)
    txt_brand.grid(row=0, column=1, padx=10, pady=10)

    active = ttk.BooleanVar(value=True)

    ttk.Checkbutton(
        info,
        text="Active",
        variable=active
    ).grid(row=1, column=1, sticky=W, padx=10)

    columns = ("ID", "Brand", "Status")

    tree = tkttk.Treeview(
        main,
        columns=columns,
        show="headings",
        height=12
    )

    tree.heading("ID", text="ID")
    tree.heading("Brand", text="Brand Name")
    tree.heading("Status", text="Status")

    tree.column("ID", width=70, anchor=CENTER)
    tree.column("Brand", width=350)
    tree.column("Status", width=120, anchor=CENTER)

    def load_brands():

        for row in tree.get_children():
            tree.delete(row)

        rows = get_brands()

        for row in rows:
            tree.insert("", END, values=row)

    def clear_form():
        txt_brand.delete(0, END)
        active.set(True)

    def save_brand():

        name = txt_brand.get().strip()

        if name == "":
            messagebox.showerror(
                "Error",
                "Brand Name is required."
            )
            return

        if brand_exists(name):
            messagebox.showwarning(
                "Duplicate",
                "Brand already exists."
            )
            return

        status = "Active" if active.get() else "Inactive"

        ok = add_brand(name, status)

        if ok:
            messagebox.showinfo(
                "Success",
                "Brand Saved Successfully."
            )

            clear_form()
            load_brands()
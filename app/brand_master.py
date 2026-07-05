import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import ttk as tkttk
from tkinter import messagebox

from database.brand_db import (
    add_brand,
    get_brands,
    brand_exists,
    search_brands,
)

def show_brand_master(parent):

    for widget in parent.winfo_children():
        widget.destroy()

    main = ttk.Frame(parent)
    main.pack(fill=BOTH, expand=True, padx=20, pady=20)

    ttk.Label(
        main,
        text="BRAND MASTER",
        font=("Segoe UI", 20, "bold")
    ).pack(anchor=W, pady=(0, 20))

    # ==========================
    # Form
    # ==========================

    info = ttk.LabelFrame(main, text="Brand Information")
    info.pack(fill=X, pady=(0, 15))

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
    ).grid(row=1, column=1, padx=10, sticky=W)

    # ==========================
    # Buttons
    # ==========================

       # ==========================
    # Search
    # ==========================

    search_frame = ttk.Frame(main)
    search_frame.pack(fill=X, pady=(0, 10))

    ttk.Label(
        search_frame,
        text="Search"
    ).pack(side=LEFT)

    txt_search = ttk.Entry(
        search_frame,
        width=30
    )

    txt_search.pack(side=LEFT, padx=5)
ttk.Button(
    search_frame,
    text="Search",
    bootstyle=PRIMARY,
    command=search_brand
).pack(side=LEFT, padx=5)
  btn_frame = ttk.Frame(main)
btn_frame.pack(fill=X, pady=10)
    # ==========================
    # Table
    # ==========================

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

    tree.column("ID", width=80, anchor=CENTER)
    tree.column("Brand", width=350)
    tree.column("Status", width=120, anchor=CENTER)

    tree.pack(fill=BOTH, expand=True)

    # ==========================
    # Functions
    # ==========================

    def load_brands():

        for item in tree.get_children():
            tree.delete(item)

        rows = get_brands()

        for row in rows:
            tree.insert("", END, values=row)

    def search_brand():

    keyword = txt_search.get().strip()

    rows = search_brands(keyword)

    for item in tree.get_children():
        tree.delete(item)

    for row in rows:
        tree.insert("", END, values=row)
        txt_brand.delete(0, END)
        active.set(True)
        txt_brand.focus()

    def save_brand():

        name = txt_brand.get().strip()

        if name == "":
            messagebox.showerror(
                "Error",
                "Please enter Brand Name."
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
                "Brand saved successfully."
            )
            clear_form()
            load_brands()
        else:
            messagebox.showerror(
                "Error",
                "Unable to save brand."
            )

    # ==========================
    # Buttons
    # ==========================

    ttk.Button(
        btn_frame,
        text="Save",
        bootstyle=SUCCESS,
        command=save_brand
    ).pack(side=LEFT, padx=5)

    ttk.Button(
        btn_frame,
        text="Clear",
        bootstyle=WARNING,
        command=clear_form
    ).pack(side=LEFT, padx=5)

    ttk.Button(
        btn_frame,
        text="Refresh",
        bootstyle=INFO,
        command=load_brands
    ).pack(side=LEFT, padx=5)

    # ==========================
    # Initial Load
    # ==========================

    load_brands()
    txt_brand.focus()
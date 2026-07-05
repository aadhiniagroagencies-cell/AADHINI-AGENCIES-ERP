import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from tkinter import ttk as tkttk

from database.products_db import add_product, get_products
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

from database.products_db import add_product


def show_products(parent):

    # Clear existing widgets
    for widget in parent.winfo_children():
        widget.destroy()

    # Main Frame
    form = ttk.Frame(parent, padding=20)
    form.pack(fill=BOTH, expand=True)

    # Heading
    ttk.Label(
        form,
        text="Product Master",
        font=("Segoe UI", 20, "bold"),
        bootstyle="primary"
    ).grid(row=0, column=0, columnspan=2, pady=(0, 20))

    labels = [
        "Product Code",
        "Product Name",
        "Brand",
        "Category",
        "Unit",
        "Purchase Price",
        "Selling Price",
        "GST %"
    ]

    entries = []

    # Input Fields
    for i, text in enumerate(labels):

        ttk.Label(
            form,
            text=text,
            font=("Segoe UI", 11)
        ).grid(row=i + 1, column=0, padx=10, pady=8, sticky=W)

        entry = ttk.Entry(
            form,
            width=35
        )

        entry.grid(
            row=i + 1,
            column=1,
            padx=10,
            pady=8,
            sticky=W
        )

        entries.append(entry)

    # Save Function
    def save_product():

        data = [e.get() for e in entries]

        if data[0] == "" or data[1] == "":
            messagebox.showerror(
                "Error",
                "Product Code and Product Name are required."
            )
            return

        try:
            add_product(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                float(data[5] or 0),
                float(data[6] or 0),
                float(data[7] or 0)
            )

            messagebox.showinfo(
                "Success",
                "Product Saved Successfully."
            )

            for e in entries:
                e.delete(0, END)

        except Exception as ex:
            messagebox.showerror(
                "Error",
                str(ex)
            )

    # Save Button
    ttk.Button(
        form,
        text="💾 Save Product",
        bootstyle="success",
        command=save_product,
        width=25
    ).grid(row=10, column=0, columnspan=2, pady=25)
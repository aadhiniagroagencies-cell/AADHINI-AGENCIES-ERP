import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from app.product_master import show_products
from app.brand_master import show_brand_master
from database.db_manager import initialize_database


# --------------------------------------------------
# Initialize Database
# --------------------------------------------------
initialize_database()


# --------------------------------------------------
# Main Window
# --------------------------------------------------
root = ttk.Window(themename="flatly")
root.title("AADHINI ERP")
root.geometry("1200x700")


# --------------------------------------------------
# Header
# --------------------------------------------------
header = ttk.Frame(root, bootstyle="primary")
header.pack(fill=X)

title = ttk.Label(
    header,
    text="AADHINI ERP",
    font=("Segoe UI", 22, "bold"),
    bootstyle="inverse-primary"
)
title.pack(pady=12)


# --------------------------------------------------
# Left Menu
# --------------------------------------------------
menu = ttk.Frame(root, width=220, bootstyle="dark")
menu.pack(side=LEFT, fill=Y)


# --------------------------------------------------
# Content Area
# --------------------------------------------------
content = ttk.Frame(root)
content.pack(side=RIGHT, expand=True, fill=BOTH)


# --------------------------------------------------
# Dashboard
# --------------------------------------------------
def show_dashboard():

    for widget in content.winfo_children():
        widget.destroy()

    ttk.Label(
        content,
        text="Welcome to AADHINI ERP",
        font=("Segoe UI", 26, "bold")
    ).pack(pady=80)

    ttk.Label(
        content,
        text="Hardware | Electrical | Agro | Paints | Billing | Inventory",
        font=("Segoe UI", 12)
    ).pack()


# --------------------------------------------------
# Placeholder Pages
# --------------------------------------------------
def placeholder(page):

    for widget in content.winfo_children():
        widget.destroy()

    ttk.Label(
        content,
        text=f"{page}\n\nComing Soon",
        font=("Segoe UI", 22, "bold")
    ).pack(pady=120)


# --------------------------------------------------
# Menu Items
# --------------------------------------------------
buttons = [
    "Dashboard",
    "Products",
    "Brands",
    "Dealers",
    "Customers",
    "Purchase",
    "Sales",
    "Inventory",
    "Reports",
    "Settings"
]


# --------------------------------------------------
# Create Buttons
# --------------------------------------------------
for item in buttons:

    if item == "Dashboard":
        command = show_dashboard

    elif item == "Products":
        command = lambda: show_products(content)

    elif item == "Brands":
        command = lambda: show_brand_master(content)

    elif item == "Dealers":
        command = lambda: placeholder("Dealers")

    elif item == "Customers":
        command = lambda: placeholder("Customers")

    elif item == "Purchase":
        command = lambda: placeholder("Purchase")

    elif item == "Sales":
        command = lambda: placeholder("Sales")

    elif item == "Inventory":
        command = lambda: placeholder("Inventory")

    elif item == "Reports":
        command = lambda: placeholder("Reports")

    elif item == "Settings":
        command = lambda: placeholder("Settings")

    ttk.Button(
        menu,
        text=item,
        command=command,
        width=22,
        bootstyle="secondary"
    ).pack(fill=X, padx=10, pady=5)


# --------------------------------------------------
# Show Dashboard
# --------------------------------------------------
show_dashboard()


# --------------------------------------------------
# Start Application
# --------------------------------------------------
root.mainloop()
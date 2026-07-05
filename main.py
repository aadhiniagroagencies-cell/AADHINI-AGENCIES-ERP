import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from app.products import show_products

# -----------------------------
# Create Main Window
# -----------------------------
root = ttk.Window(themename="flatly")
root.title("AADHINI ERP")
root.geometry("1200x700")

# -----------------------------
# Header
# -----------------------------
header = ttk.Frame(root, bootstyle="primary", height=60)
header.pack(fill=X)

title = ttk.Label(
    header,
    text="AADHINI ERP",
    font=("Segoe UI", 22, "bold"),
    bootstyle="inverse-primary"
)
title.pack(pady=12)

# -----------------------------
# Main Content Area
# -----------------------------
content = ttk.Frame(root)
content.pack(side=RIGHT, expand=True, fill=BOTH)

welcome = ttk.Label(
    content,
    text="Welcome to AADHINI ERP",
    font=("Segoe UI", 24, "bold")
)
welcome.pack(pady=100)

# -----------------------------
# Left Menu
# -----------------------------
menu = ttk.Frame(root, bootstyle="dark", width=220)
menu.pack(side=LEFT, fill=Y)

buttons = [
    "Dashboard",
    "Products",
    "Dealers",
    "Customers",
    "Purchase",
    "Sales",
    "Inventory",
    "Reports",
    "Settings"
]

def show_dashboard():
    for widget in content.winfo_children():
        widget.destroy()

    ttk.Label(
        content,
        text="Welcome to AADHINI ERP",
        font=("Segoe UI", 24, "bold")
    ).pack(pady=100)

for item in buttons:

    if item == "Dashboard":
        action = show_dashboard

    elif item == "Products":
        action = lambda: show_products(content)

    else:
        action = None

    ttk.Button(
        menu,
        text=item,
        command=action,
        width=20,
        bootstyle="secondary"
    ).pack(pady=5, padx=10, fill=X)

root.mainloop()
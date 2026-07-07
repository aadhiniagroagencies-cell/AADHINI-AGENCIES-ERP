"""
AADHINI ERP Enterprise
Base View

Common UI helper for all master screens.
"""

import ttkbootstrap as ttk
from tkinter import messagebox


class BaseView(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

    # ---------------------------------------------------------
    # Message Helpers
    # ---------------------------------------------------------

    def show_success(self, message):
        messagebox.showinfo("Success", message)

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def show_warning(self, message):
        messagebox.showwarning("Warning", message)

    # ---------------------------------------------------------
    # Confirmation
    # ---------------------------------------------------------

    def confirm_delete(self):
        return messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this record?"
        )

    # ---------------------------------------------------------
    # Entry Helpers
    # ---------------------------------------------------------

    def clear_entries(self, entries):

        for widget in entries:

            try:
                widget.delete(0, "end")
            except Exception:
                pass

    # ---------------------------------------------------------
    # Text Widget Helpers
    # ---------------------------------------------------------

    def clear_text(self, text_widget):

        text_widget.delete("1.0", "end")

    # ---------------------------------------------------------
    # Grid Helpers
    # ---------------------------------------------------------

    def refresh_grid(self, grid, rows):

        grid.load(rows)
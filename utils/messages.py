from tkinter import messagebox


def success(msg):
    messagebox.showinfo("Success", msg)


def error(msg):
    messagebox.showerror("Error", msg)


def warning(msg):
    messagebox.showwarning("Warning", msg)


def ask_delete():
    return messagebox.askyesno(
        "Confirm",
        "Are you sure you want to delete this record?"
    )
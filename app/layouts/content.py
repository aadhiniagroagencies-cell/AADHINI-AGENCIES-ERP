"""
AADHINI ERP Enterprise
Workspace / Content Area
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Content(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.configure(padding=20)

        # Workspace where screens will load
        self.workspace = ttk.Frame(self)
        self.workspace.pack(fill=BOTH, expand=True)

        # Show dashboard initially
        self.show_dashboard()

    def clear_workspace(self):
        """Remove all widgets from workspace"""
        for widget in self.workspace.winfo_children():
            widget.destroy()

    def show_dashboard(self):

        self.clear_workspace()

        title = ttk.Label(
            self.workspace,
            text="Dashboard",
            font=("Segoe UI", 24, "bold")
        )

        title.pack(anchor="w", pady=(0, 20))

        welcome = ttk.Label(
            self.workspace,
            text="Welcome to AADHINI ERP Enterprise",
            font=("Segoe UI", 12)
        )

        welcome.pack(anchor="w")

        separator = ttk.Separator(
            self.workspace,
            orient="horizontal"
        )

        separator.pack(fill=X, pady=20)

        info = ttk.Label(
            self.workspace,
            text="Dashboard widgets will be displayed here.",
            font=("Segoe UI", 11)
        )

        info.pack(anchor="w")

    def show_view(self, view_class):
        """Load any screen inside the workspace"""

        self.clear_workspace()

        view = view_class(self.workspace)

        view.pack(fill=BOTH, expand=True)
"""
AADHINI ERP Enterprise
Base Master Screen
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from app.widgets.form_header import FormHeader
from app.widgets.form_buttons import FormButtons
from app.widgets.search_bar import SearchBar
from app.widgets.data_grid import DataGrid


class BaseMaster(ttk.Frame):

    def __init__(
        self,
        parent,
        title,
        subtitle,
        columns,
        save_command=None,
        update_command=None,
        delete_command=None,
        clear_command=None,
        search_command=None
    ):
        super().__init__(parent)

        self.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # Header
        FormHeader(
            self,
            title,
            subtitle
        )

        # Form Area
        self.form = ttk.LabelFrame(
            self,
            text="Information"
        )

        self.form.pack(fill=X)

        # Buttons
        FormButtons(
            self,
            save_command,
            update_command,
            delete_command,
            clear_command
        )

        # Search
        self.search = SearchBar(
            self,
            search_command
        )

        # Grid
        self.grid = DataGrid(
            self,
            columns
        )
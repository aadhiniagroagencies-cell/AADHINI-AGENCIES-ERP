"""
AADHINI ERP Enterprise
Application
"""

import ttkbootstrap as ttk

from app.core.config import Config
from app.layouts.main_layout import MainLayout


class AadhiniERP(ttk.Window):

    def __init__(self):
        super().__init__(themename=Config.THEME)

        self.title(f"{Config.APP_NAME}  v{Config.VERSION}")

        self.geometry(
            f"{Config.WINDOW_WIDTH}x{Config.WINDOW_HEIGHT}"
        )

        self.state("zoomed")

        MainLayout(self)
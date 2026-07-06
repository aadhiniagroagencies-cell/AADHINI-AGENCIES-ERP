"""
AADHINI ERP Enterprise
Main Layout
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from app.layouts.header import Header
from app.layouts.sidebar import Sidebar
from app.layouts.content import Content
from app.layouts.statusbar import StatusBar


class MainLayout(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.pack(fill=BOTH, expand=True)

        self.build_ui()

    def build_ui(self):

        # ---------------- Header ----------------
        header = Header(self)
        header.pack(fill=X)

        # ---------------- Body ----------------
        body = ttk.Frame(self)
        body.pack(fill=BOTH, expand=True)

        # Sidebar
        sidebar = Sidebar(body)
        sidebar.pack(side=LEFT, fill=Y)

        # Content Area
        content = Content(body)
        content.pack(side=LEFT, fill=BOTH, expand=True)

        # ---------------- Status Bar ----------------
        status = StatusBar(self)
        status.pack(fill=X)
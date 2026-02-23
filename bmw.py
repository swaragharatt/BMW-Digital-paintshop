import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QFrame, QGridLayout, QStackedWidget)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QColor, QPalette, QLinearGradient, QBrush, QPixmap

class BMWConfigurator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BMW Digital Paintshop")
        self.resize(1200, 800)
        self.setStyleSheet("background-color: #0a0a0a; color: white;")
        
        self.active_tab = "Paint"
        self.selections = {
            "Paint": "M Portimao Blue",
            "Wheels": "19\"/20\" M Double-spoke 826 M",
            "Interior": "Leather 'Merino' Black",
            "Price": 84200
        }

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.nav_buttons = {}
        self.setup_nav_bar()
        self.setup_content_area()
        self.setup_footer()

    def setup_nav_bar(self):
        nav_bar = QFrame()
        nav_bar.setFixedHeight(80)
        nav_bar.setStyleSheet("QFrame { border-bottom: 1px solid #222; background-color: #0a0a0a; }")
        nav_layout = QHBoxLayout(nav_bar)
        nav_layout.setContentsMargins(40, 0, 40, 0)

        logo_container = QHBoxLayout()
        logo_label = QLabel("BMW")
        logo_label.setStyleSheet("font-weight: bold; font-size: 24px; letter-spacing: -1px;")
        
        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.VLine)
        divider.setFixedWidth(1)
        divider.setStyleSheet("background-color: #444; margin: 20px 0;")
        
        title_label = QLabel("DIGITAL PAINTSHOP")
        title_label.setStyleSheet("font-size: 18px; letter-spacing: 2px; color: #eee; font-weight: 300;")
        
        logo_container.addWidget(logo_label)
        logo_container.addWidget(divider)
        logo_container.addWidget(title_label)
        nav_layout.addLayout(logo_container)

        nav_layout.addStretch()

        tabs = ["Paint", "Wheels", "Interior", "Summary"]
        for tab in tabs:
            btn = QPushButton(tab)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(lambda checked, t=tab: self.switch_tab(t))
            self.nav_buttons[tab] = btn
            nav_layout.addWidget(btn)
        
        self.update_nav_styles()

        nav_layout.addStretch()

        self.price_display = QLabel(f"€ {self.selections['Price']:,}.00")
        self.price_display.setStyleSheet("font-size: 20px; font-weight: 300; margin-right: 20px;")
        nav_layout.addWidget(self.price_display)

        cta_btn = QPushButton("ORDER NOW")
        cta_btn.setFixedSize(160, 45)
        cta_btn.setStyleSheet("""
            QPushButton {
                background-color: #1c69d4;
                color: white;
                font-weight: bold;
                border: none;
                font-size: 12px;
                letter-spacing: 1px;
            }
            QPushButton:hover { background-color: #2a7be6; }
        """)
        nav_layout.addWidget(cta_btn)

        self.main_layout.addWidget(nav_bar)

    def update_nav_styles(self):
        for name, btn in self.nav_buttons.items():
            active = "border-bottom: 2px solid #0066ff; color: white;" if name == self.active_tab else "color: #888; border-bottom: 2px solid transparent;"
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: none;
                    border: none;
                    font-size: 14px;
                    font-weight: bold;
                    text-transform: uppercase;
                    padding: 30px 15px;
                    {active}
                }}
                QPushButton:hover {{ color: white; }}
            """)

    def setup_content_area(self):
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(60, 60, 60, 40)

        info_box = QFrame()
        info_box.setFixedSize(450, 220)
        info_box.setStyleSheet("QFrame { background-color: rgba(0, 0, 0, 0.6); border: 1px solid #222; }")
        info_layout = QVBoxLayout(info_box)
        info_layout.setContentsMargins(30, 30, 30, 30)

        model_name = QLabel("THE M4")
        model_name.setStyleSheet("font-size: 32px; font-weight: 300; border: none;")
        sub_name = QLabel("COUPÉ COMPETITION")
        sub_name.setStyleSheet("font-size: 12px; color: #888; letter-spacing: 2px; border: none;")
        
        info_layout.addWidget(model_name)
        info_layout.addWidget(sub_name)
        info_layout.addSpacing(20)

        def create_stat_row(label, value):
            row = QHBoxLayout()
            l = QLabel(label)
            l.setStyleSheet("color: #666; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; border: none;")
            v = QLabel(value)
            v.setStyleSheet("font-weight: bold; font-size: 12px; border: none;")
            row.addWidget(l)
            row.addStretch()
            row.addWidget(v)
            return row

        info_layout.addLayout(create_stat_row("ACCELERATION", "3.9S (0-100 KM/H)"))
        sep = QFrame(); sep.setFixedHeight(1); sep.setStyleSheet("background-color: #222; border: none;")
        info_layout.addWidget(sep)
        info_layout.addLayout(create_stat_row("POWER", "375 KW (510 HP)"))
        
        layout.addWidget(info_box)

        car_display = QLabel()
        car_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(r"D:\USER DATA\Downloads\eb8d551b8efccec38a91563a54fa4327.jpg")
        car_display.setPixmap(pixmap.scaled(700, 400, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        layout.addWidget(car_display)

        layout.addStretch()

        self.stack = QStackedWidget()
        self.stack.setFixedWidth(500)
        self.stack.setFixedHeight(350)
        
        self.stack.addWidget(self.create_paint_panel())
        self.stack.addWidget(self.create_wheels_panel())
        self.stack.addWidget(self.create_interior_panel())
        self.stack.addWidget(self.create_summary_panel())

        bottom_row = QHBoxLayout()
        bottom_row.addStretch()
        bottom_row.addWidget(self.stack)
        layout.addLayout(bottom_row)

        self.main_layout.addWidget(content)

    def create_panel_base(self, title, selection_key):
        panel = QFrame()
        panel.setStyleSheet("QFrame { background-color: rgba(0, 0, 0, 0.85); border: 1px solid #222; }")
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(30, 25, 30, 25)

        header = QHBoxLayout()
        title_label = QLabel(title)
        title_label.setStyleSheet("font-size: 18px; font-weight: 300; border: none; letter-spacing: 2px;")
        
        self.selection_labels = getattr(self, 'selection_labels', {})
        sel_label = QLabel(self.selections[selection_key])
        sel_label.setStyleSheet("color: #1c69d4; font-size: 11px; border: none;")
        self.selection_labels[selection_key] = sel_label
        
        header.addWidget(title_label)
        header.addStretch()
        header.addWidget(sel_label)
        layout.addLayout(header)
        layout.addSpacing(20)
        
        return panel, layout

    def create_paint_panel(self):
        panel, layout = self.create_panel_base("EXTERIOR PAINT", "Paint")
        grid = QGridLayout()
        paints = [
            ("#1a3a6e", "M Portimao Blue"), ("#3d3d3d", "Frozen Deep Grey"), 
            ("#1b3022", "San Remo Green"), ("#8b0000", "Fire Red"),
            ("#8e908f", "Skyscraper Grey"), ("#0a0a0a", "Black Sapphire"), 
            ("#ffffff", "Alpine White"), ("#004d40", "Isle of Man Green")
        ]
        for i, (hex_code, name) in enumerate(paints):
            btn = QPushButton()
            btn.setFixedSize(85, 85)
            active = name == self.selections["Paint"]
            btn.setStyleSheet(f"background-color: {hex_code}; border: {'4px solid #1c69d4' if active else '1px solid #333'};")
            btn.clicked.connect(lambda checked, n=name: self.update_selection("Paint", n))
            grid.addWidget(btn, i // 4, i % 4)
        layout.addLayout(grid)
        return panel

    def create_wheels_panel(self):
        panel, layout = self.create_panel_base("WHEELS", "Wheels")
        options = [
            "19\"/20\" M Double-spoke 826 M",
            "19\"/20\" M Double-spoke 825 M Bicolour",
            "19\"/20\" M Forged Performance Wheels"
        ]
        for opt in options:
            btn = QPushButton(opt)
            active = opt == self.selections["Wheels"]
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {'#1c69d4' if active else '#111'};
                    color: white; border: 1px solid #333; padding: 15px; text-align: left; font-size: 12px;
                }}
                QPushButton:hover {{ background-color: #222; }}
            """)
            btn.clicked.connect(lambda checked, o=opt: self.update_selection("Wheels", o))
            layout.addWidget(btn)
        layout.addStretch()
        return panel

    def create_interior_panel(self):
        panel, layout = self.create_panel_base("INTERIOR", "Interior")
        options = ["Leather 'Merino' Black", "Leather 'Merino' Yas Marina Blue", "Leather 'Merino' Silverstone"]
        for opt in options:
            btn = QPushButton(opt)
            active = opt == self.selections["Interior"]
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {'#1c69d4' if active else '#111'};
                    color: white; border: 1px solid #333; padding: 15px; text-align: left; font-size: 12px;
                }}
            """)
            btn.clicked.connect(lambda checked, o=opt: self.update_selection("Interior", o))
            layout.addWidget(btn)
        layout.addStretch()
        return panel

    def create_summary_panel(self):
        panel = QFrame()
        panel.setStyleSheet("QFrame { background-color: rgba(0, 0, 0, 0.9); border: 1px solid #1c69d4; }")
        self.summary_layout = QVBoxLayout(panel)
        self.summary_layout.setContentsMargins(30, 30, 30, 30)
        self.refresh_summary()
        return panel

    def refresh_summary(self):
        while self.summary_layout.count():
            item = self.summary_layout.takeAt(0)
            if item.widget(): item.widget().deleteLater()
            
        title = QLabel("YOUR CONFIGURATION")
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #1c69d4; border: none;")
        self.summary_layout.addWidget(title)
        self.summary_layout.addSpacing(20)
        
        for key in ["Paint", "Wheels", "Interior"]:
            row = QHBoxLayout()
            l = QLabel(key.upper())
            l.setStyleSheet("color: #666; font-size: 10px; border: none;")
            v = QLabel(self.selections[key])
            v.setStyleSheet("font-size: 13px; border: none;")
            row.addWidget(l)
            row.addStretch()
            row.addWidget(v)
            self.summary_layout.addLayout(row)
            
        sep = QFrame(); sep.setFixedHeight(1); sep.setStyleSheet("background-color: #333; margin: 10px 0; border: none;")
        self.summary_layout.addWidget(sep)
        
        total = QHBoxLayout()
        tl = QLabel("TOTAL PRICE")
        tl.setStyleSheet("font-weight: bold; border: none;")
        tv = QLabel(f"€ {self.selections['Price']:,}.00")
        tv.setStyleSheet("font-size: 18px; font-weight: bold; color: #1c69d4; border: none;")
        total.addWidget(tl)
        total.addStretch()
        total.addWidget(tv)
        self.summary_layout.addLayout(total)
        self.summary_layout.addStretch()

    def switch_tab(self, name):
        self.active_tab = name
        mapping = {"Paint": 0, "Wheels": 1, "Interior": 2, "Summary": 3}
        self.stack.setCurrentIndex(mapping[name])
        self.update_nav_styles()
        if name == "Summary":
            self.refresh_summary()

    def update_selection(self, key, value):
        self.selections[key] = value
        if hasattr(self, 'selection_labels') and key in self.selection_labels:
            self.selection_labels[key].setText(value)
        idx = self.stack.currentIndex()
        self.stack.removeWidget(self.stack.widget(idx))
        if key == "Paint": self.stack.insertWidget(0, self.create_paint_panel())
        elif key == "Wheels": self.stack.insertWidget(1, self.create_wheels_panel())
        elif key == "Interior": self.stack.insertWidget(2, self.create_interior_panel())
        self.stack.setCurrentIndex(idx)

    def setup_footer(self):
        footer = QFrame()
        footer.setFixedHeight(40)
        footer.setStyleSheet("background-color: #0a0a0a; border-top: 1px solid #111;")
        footer_layout = QHBoxLayout(footer)
        footer_layout.setContentsMargins(40, 0, 40, 0)

        legal_label = QLabel("LEGAL NOTICE   |   COOKIE POLICY   |   TECHNICAL DATA")
        legal_label.setStyleSheet("color: #444; font-size: 10px; font-weight: bold; letter-spacing: 1px;")
        
        specs_label = QLabel("BMW M4 COMPETITION COUPÉ: 10.2 - 10.0 L/100 KM | 233 - 227 G CO2/KM")
        specs_label.setStyleSheet("color: #444; font-size: 10px; font-weight: bold; letter-spacing: 1px;")

        footer_layout.addWidget(legal_label)
        footer_layout.addStretch()
        footer_layout.addWidget(specs_label)
        self.main_layout.addWidget(footer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI", 10))
    window = BMWConfigurator()
    window.show()
    sys.exit(app.exec())

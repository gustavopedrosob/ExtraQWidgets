import sys

import qtawesome
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout

from extra_qwidgets.widgets.color_button import QColorButton
from source.extra_qwidgets.utils import colorize_icon_by_theme


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Color Button Test")
        self.setWindowIcon(colorize_icon_by_theme(qtawesome.icon("fa6b.python")))

        widget = QWidget()

        layout = QVBoxLayout()

        color_button_1 = QColorButton("Color Button 1", "#0077B6")
        color_button_2 = QColorButton("Color Button 2", "#CC2936")
        color_button_3 = QColorButton("Color Button 3", "#C5D86D", "#000000")
        layout.addWidget(color_button_1)
        layout.addWidget(color_button_2)
        layout.addWidget(color_button_3)

        widget.setLayout(layout)

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from source.extra_qwidgets.widgets import QPassword
from source.extra_qwidgets.utils import get_awesome_icon, colorize_icon_by_theme


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Test")
        self.setWindowIcon(colorize_icon_by_theme(get_awesome_icon("python", "brands")))

        widget = QPassword()

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
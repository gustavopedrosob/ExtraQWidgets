from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication

from widgets.resposive_text_edit import QResponsiveTextEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit Auto-ajustável")

        self.text_edit = QResponsiveTextEdit()
        self.text_edit.setPlaceholderText("Digite algo...")
        self.text_edit.setMaximumHeight(500)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
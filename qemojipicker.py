import emojis.db
from PySide6.QtCore import QEvent
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QLabel, QGridLayout, QVBoxLayout, QPushButton, \
    QScrollArea
from emojis.db import Emoji

from utils import is_dark_mode, colorize_icon


class QColorResponsiveButton(QPushButton):
    def __init__(self, parent=None):
        super(QColorResponsiveButton, self).__init__(parent)
        self.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.PaletteChange:
            self.setIcon(self.icon())
        return super().eventFilter(obj, event)

    def setIcon(self, icon):
        if is_dark_mode():
            icon = colorize_icon(icon, "#FFFFFF")
        super().setIcon(icon)



class QCollapseGroup(QWidget):
    def __init__(self, title: str, widget: QWidget):
        super().__init__()
        self.__collapsed = False
        self.__widget = widget
        self.__collapse_button = QColorResponsiveButton()
        self.__collapse_button.setIcon(QIcon("assets/icons/angle-down-solid.svg"))
        self.__collapse_button.setFlat(True)
        self.__collapse_button.clicked.connect(self.__collapse)
        self.__label = QLabel(title)
        self.__header_layout = QHBoxLayout()
        self.__header_layout.addWidget(self.__collapse_button)
        self.__header_layout.addWidget(self.__label)
        self.__header_layout.setStretch(1, True)
        self.__layout = QVBoxLayout()
        self.__layout.addLayout(self.__header_layout)
        self.__layout.addWidget(widget)
        self.setLayout(self.__layout)

    def __collapse(self):
        if self.__collapsed:
            self.__widget.show()
            self.__collapse_button.setIcon(QIcon("assets/icons/angle-down-solid.svg"))
        else:
            self.__widget.hide()
            self.__collapse_button.setIcon(QIcon("assets/icons/angle-right-solid.svg"))
        self.__collapsed = not self.__collapsed

    def widget(self):
        return self.__widget



class QEmojiGrid(QWidget):
    font = QFont()
    font.setPointSize(20)

    def __init__(self):
        super().__init__()
        self.__grid_layout = QGridLayout()
        self.setLayout(self.__grid_layout)

    def add_emoji(self, emoji: Emoji):
        button = QPushButton(emoji.emoji)
        button.setFlat(True)
        button.setFont(self.font)
        children_count = self.layout().count()
        row = children_count // 9
        column = children_count % 9
        self.__grid_layout.addWidget(button, row, column)


class QEmojiPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.__line_edit = QLineEdit()
        self.__line_edit.setPlaceholderText("Enter your favorite emoji")
        self.__categories = {}
        self.__current_emoji_label = QLabel()
        self.__menu_horizontal_layout = QHBoxLayout()
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        content_widget = QWidget()
        self.__collapse_groups_layout = QVBoxLayout(content_widget)
        scroll_area.setWidget(content_widget)
        self.__vertical_layout = QVBoxLayout()
        self.__vertical_layout.addLayout(self.__menu_horizontal_layout)
        self.__vertical_layout.addWidget(self.__line_edit)
        self.__vertical_layout.addWidget(content_widget)
        self.__vertical_layout.addWidget(self.__current_emoji_label)
        self.setLayout(self.__vertical_layout)
        self.add_category("Smileys & Emotion", QIcon("assets/icons/face-smile-solid.svg"))
        self.__insert_emojis("Smileys & Emotion")

    def add_category(self, category: str, icon: QIcon):
        button = QPushButton()
        button.setIcon(icon)
        self.__menu_horizontal_layout.addWidget(button)
        collapse_group = QCollapseGroup(category, QEmojiGrid())
        self.__categories[category] = collapse_group
        self.__collapse_groups_layout.addWidget(collapse_group)

    def emoji_grid(self, category: str) -> QEmojiGrid:
        return self.__categories[category].widget()

    def __insert_emojis(self, category: str):
        emoji_grid = self.emoji_grid(category)
        for emoji in emojis.db.get_emojis_by_category(category):
            emoji_grid.add_emoji(emoji)

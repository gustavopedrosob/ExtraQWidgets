import typing
from pathlib import Path

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPainter, QPixmap, QColor, Qt
from PySide6.QtWidgets import QApplication
from emojis.db import Emoji


def adjust_brightness(hex_color: str, percentage: float = 10) -> str:
    """
    Ajusta o brilho de uma cor hexadecimal.

    Args:
        hex_color (str): Cor no formato hexadecimal (e.g., '#RRGGBB').
        percentage (float): Porcentagem para ajustar o brilho (positivo para mais brilho, negativo para menos).

    Returns:
        str: Nova cor no formato hexadecimal com o brilho ajustado.
    """
    # Remover o símbolo '#' se presente
    hex_color = hex_color.lstrip("#")

    # Converter o hexadecimal para valores RGB
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)

    # Calcular o fator de ajuste
    factor = 1 + (percentage / 100)

    # Aplicar o ajuste e garantir que os valores fiquem no intervalo [0, 255]
    r = min(255, max(0, int(r * factor)))
    g = min(255, max(0, int(g * factor)))
    b = min(255, max(0, int(b * factor)))

    # Converter de volta para hexadecimal
    return f"#{r:02X}{g:02X}{b:02X}"


def is_dark_mode() -> bool:
    style_hints = QApplication.styleHints()
    color_scheme = style_hints.colorScheme()
    return color_scheme.value == 2


def colorize_pixmap(pixmap: QPixmap, color: str) -> QPixmap:
    # Create a new QPixmap with the same size and fill it with transparent color
    colored_pixmap = QPixmap(pixmap.size())
    colored_pixmap.fill(Qt.GlobalColor.transparent)

    # Paint the original pixmap onto the new pixmap with the desired color
    painter = QPainter(colored_pixmap)
    painter.drawPixmap(0, 0, pixmap)
    painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
    painter.fillRect(colored_pixmap.rect(), QColor(color))
    painter.end()

    # Convert the colored QPixmap back to QIcon
    return colored_pixmap


def get_all_pixmap_from_icon(icon: QIcon, size: QSize = QSize(64, 64)) -> typing.Dict[typing.Tuple[QIcon.Mode, QIcon.State], QPixmap]:
    modes = [QIcon.Mode.Normal, QIcon.Mode.Disabled, QIcon.Mode.Active, QIcon.Mode.Selected]
    states = [QIcon.State.Off, QIcon.State.On]
    all_pixmap = {}
    for mode in modes:
        for state in states:
            pixmap = icon.pixmap(size, mode, state)
            if not pixmap.isNull():
                key = (mode, state)
                all_pixmap[key] = pixmap
    return all_pixmap


def colorize_icon(icon: QIcon, color: str, size: QSize = QSize(64, 64)) -> QIcon:
    new_icon = QIcon()
    for key, value in get_all_pixmap_from_icon(icon, size).items():
        mode, state = key
        pixmap = icon.pixmap(size, mode, state)
        new_icon.addPixmap(colorize_pixmap(pixmap, color), mode, state)
    return new_icon


def colorize_icon_by_theme(icon: QIcon, size: QSize = QSize(64, 64)) -> QIcon:
    color = "#FFFFFF" if is_dark_mode() else "#000000"
    return colorize_icon(icon, color, size)


def get_emoji_path(emoji: Emoji) -> str:
    file_name = emoji_to_code_point(emoji)
    path = Path(__file__).parent.absolute() / f"assets/emojis/{file_name}.png"
    if path.exists():
        return str(path)
    else:
        file_name = "-".join(file_name.split("-")[:-1])
        path = Path(__file__).parent.absolute() / f"assets/emojis/{file_name}.png"
        return str(path)


def emoji_to_code_point(emoji: Emoji):
    delimiter = "-"
    # Convert the string into a list of UTF-16 code units
    code_units = [ord(char) for char in emoji.emoji]

    # Process the code units in pairs (high surrogate + low surrogate)
    code_points = []
    i = 0
    while i < len(code_units):
        high_surrogate = code_units[i]
        low_surrogate = code_units[i + 1] if i + 1 < len(code_units) else None

        # Check if the current pair is a valid surrogate pair
        if 0xD800 <= high_surrogate <= 0xDBFF and 0xDC00 <= low_surrogate <= 0xDFFF:
            # Calculate the code point
            code_point = (
                    ((high_surrogate - 0xD800) << 10)
                    + (low_surrogate - 0xDC00)
                    + 0x10000
            )
            code_points.append(hex(code_point)[2:])  # Remove the '0x' prefix
            i += 2  # Move to the next pair
        else:
            # If not a surrogate pair, treat it as a regular code point
            code_points.append(hex(high_surrogate)[2:])
            i += 1

    # Join the code points with the specified delimiter
    return delimiter.join(code_points)

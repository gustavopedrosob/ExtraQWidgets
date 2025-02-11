# ExtraQWidgets

This is a collection of custom widgets for PyQt6/PySide6

## Widgets

### QEmojiPicker

![QEmojiPicker](assets/imgs/QEmojiPicker.png)

A emoji picker.

```python
emoji_picker = QEmojiPicker()
```

### QCheckBoxGroup

![QCheckBoxGroup](assets/imgs/QCheckBoxGroup.png)

A group of checkboxes that can be used to select a single option.

```python
checkbox_group = QCheckBoxGroup(QLabel("Select a color:"))
checkbox_group.add_checkbox("red", QCheckBox("Red"))
checkbox_group.add_checkbox("green", QCheckBox("Green"))
checkbox_group.add_checkbox("blue", QCheckBox("Blue"))
```

### QCollapseGroup

![QCollapseGroup](assets/imgs/QCollapseGroup.png)

A group of collapsible widgets.

```python
layout = QVBoxLayout()

collapse_group = QCollapseGroup("Test", QLabel("Hello World!"))
layout.addWidget(collapse_group)
collapse_group_2 = QCollapseGroup("Test 2", QLabel("Hello World 2!"))
layout.addWidget(collapse_group_2)
```

### QColorButton

![QColorButton](assets/imgs/QColorButton.png)

A color button.

```python
color_button_1 = QColorButton("Color Button 1", "#0077B6")
color_button_2 = QColorButton("Color Button 2", "#CC2936")
color_button_3 = QColorButton("Color Button 3", "#C5D86D", "#000000")
```

### QColorResponsiveButton

![QColorResponsiveButton-light](assets/imgs/QColorResponsiveButton-light.png)
![QColorResponsiveButton-dark](assets/imgs/QColorResponsiveButton-dark.png)

A button that changes its icon color when windows theme changes.

```python
button = QColorResponsiveButton()
button.setIcon(get_icon("face-smile-solid.svg"))
```

### QPassword

![QPassword](assets/imgs/QPassword.png)

A password input with a show/hide button.

```python
password = QPassword()
```

### QResponsiveTextEdit

![QResponsiveTextEdit](assets/imgs/QResponsiveTextEdit.png)

A text edit that resizes its height based on its content.

```python
text_edit = QResponsiveTextEdit()
```

### QSingleSelectionList

![QSingleSelectionList](assets/imgs/QSingleSelectionList.png)

A interactive list of items that can be moved to a selected list of items.

```python
single_selection_list = QSingleSelectionList()
single_selection_list.add_to_select_items(["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10"])
```


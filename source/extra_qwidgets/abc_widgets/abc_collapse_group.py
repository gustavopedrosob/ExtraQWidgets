import typing
from abc import abstractmethod

from PySide6.QtWidgets import QWidget, QVBoxLayout

from extra_qwidgets.abc_widgets.abc_collapse_item import ABCCollapseItem
from extra_qwidgets.abc_widgets.abc_meta import QtABCMeta


class ABCCollapseGroup(QWidget, metaclass=QtABCMeta):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self._collapse_items = []
        self.setLayout(self.layout)

    @abstractmethod
    def _new_collapse_item(self, title: str, widget: QWidget, collapsed: bool = False, name: typing.Optional[str] = None) -> ABCCollapseItem:
        pass

    def addCollapse(self, title: str, widget: QWidget, collapsed: bool = False, name: typing.Optional[str] = None, stretch: bool = False) -> ABCCollapseItem:
        collapse_item = self._new_collapse_item(title, widget, collapsed, name)
        self.addCollapseItem(collapse_item, stretch)
        return collapse_item

    def addCollapseItem(self, collapse_item: ABCCollapseItem, stretch: bool = False):
        self.layout.addLayout(collapse_item.headerLayout())
        self.layout.addWidget(collapse_item.widget(), stretch)
        self._collapse_items.append(collapse_item)

    def removeCollapseItem(self, collapse_item):
        self.layout.removeWidget(collapse_item.header())
        self.layout.removeWidget(collapse_item.widget())
        self._collapse_items.remove(collapse_item)

    def expandAll(self):
        for item in self._collapse_items:
            item.setCollapse(False)

    def collapseAll(self):
        for item in self._collapse_items:
            item.setCollapse(True)

    def setCollapsedByTitle(self, collapse: bool, title: str):
        item = self.getItemByTitle(title)
        if item:
            item.setCollapse(collapse)

    def setCollapsedByName(self, collapse: bool, name: str):
        item = self.getItemByName(name)
        if item:
            item.setCollapse(collapse)

    def getItemByTitle(self, title: str) -> typing.Optional[ABCCollapseItem]:
        for item in self._collapse_items:
            if item.header().text() == title:
                return item
        return None

    def getItemByName(self, name: str) -> typing.Optional[ABCCollapseItem]:
        for item in self._collapse_items:
            if item.objectName() == name:
                return item
        return None

    def toggleAll(self):
        for item in self._collapse_items:
            item.setCollapse(not item.isCollapsed())

    def isAllCollapsed(self) -> bool:
        return all(item.isCollapsed() for item in self._collapse_items)

    def isAllExpanded(self) -> bool:
        return all(item.isCollapsed() is False for item in self._collapse_items)

    def items(self) -> list[ABCCollapseItem]:
        return self._collapse_items
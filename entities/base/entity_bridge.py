from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QWidget

from entities.logic.base.entity import Entity


class EntityBridge:
    entities = set()

    def __init__(self, entity_class, skin_path, parent=None):
        self.entities.add(self)
        self.parent = parent

        # Инициализация технических параметров сущности
        self.entity_logic_object = entity_class()

        # Инициализация основного графического объекта
        self.entity_graphic_object = QtEntity(
            self.entity_logic_object,
            skin_path,
            self.parent
        )
        self.entity_graphic_object.resize(*self.entity_logic_object.geometry)

        # Отрисовка сущности
        self.entity_graphic_object.show()

    @property
    def x(self):
        return self.entity_logic_object.x

    @property
    def y(self):
        return self.entity_logic_object.y

    @x.setter
    def x(self, value):
        self.entity_logic_object.x = value

    @y.setter
    def y(self, value):
        self.entity_logic_object.y = value

    def tick(self):
        self.entity_logic_object.tick()
        self.entity_graphic_object.move(self.entity_logic_object.x, self.entity_logic_object.y)

    def delete(self):
        self.entities.remove(self)
        Entity.entities.remove(self.entity_logic_object)
        self.entity_graphic_object.deleteLater()


class QtEntity(QWidget):
    def __init__(self, logic_obj_link: Entity, skin_path, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.pixmap = QPixmap(skin_path)
        self.move(logic_obj_link.x, logic_obj_link.y)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()

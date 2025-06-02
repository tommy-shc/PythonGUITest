from PyQt6.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsLineItem)
from PyQt6.QtGui import QBrush, QColor, QPen
from PyQt6.QtCore import Qt
import sys
from abc import ABC


# Simple Bus-Line-Load Network Model
# ----------------------------------

class Element(ABC):
    def __init__(self, name: str):
        self.name = name
        self.graphics_item = None

class Bus(Element):
    def __init__(self, name: str):
        super().__init__(name)

class Line(Element):
    def __init__(self, name: str, from_bus: Bus, to_bus: Bus):
        super().__init__(name)
        self.from_bus = from_bus
        self.to_bus = to_bus

class Load(Element):
    def __init__(self, name: str, bus: Bus):
        super().__init__(name)
        self.bus = bus



# GUI Viewer
# ----------

class NetworkViewer(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Network GUI")

        self.scene = QGraphicsScene(self) # QGraphicsScene provides a surface for managing 2D graphical items
        self.setScene(self.scene)

        self.build_network()

    def build_network(self):
        # dummy network
        bus1 = Bus("Bus 1")
        bus2 = Bus("Bus 2")
        line = Line("Line 1", bus1, bus2)
        load = Load("Load 1", bus1)

        # create bus items
        bus1_item = QGraphicsEllipseItem(-20, -20, 40, 40)
        bus1_item.setBrush(QBrush(QColor("blue")))
        bus1_item.setPos(100, 150)
        bus1_item.setToolTip(bus1.name) # tip is a short piece of text associated with the widget
        bus1_item.setAcceptHoverEvents(True) # text to appear when hovering over widget
        self.scene.addItem(bus1_item)
        bus1.graphics_item = bus1_item

        bus2_item = QGraphicsEllipseItem(-20, -20, 40, 40)
        bus2_item.setBrush(QBrush(QColor("blue")))
        bus2_item.setPos(300, 150)
        bus2_item.setToolTip(bus2.name)
        bus2_item.setAcceptHoverEvents(True)
        self.scene.addItem(bus2_item)
        bus2.graphics_item = bus2_item

        # create line item
        line_item = QGraphicsLineItem(bus1_item.pos().x(), bus1_item.pos().y(), bus2_item.pos().x(), bus2_item.pos().y())
        line_item.setPen(QPen(QColor("black"), 2))
        line_item.setToolTip(line.name)
        line_item.setAcceptHoverEvents(True)
        self.scene.addItem(line_item)
        line.graphics_item = line_item

        # create load item
        load_item = QGraphicsRectItem(-10, -10, 20, 20)
        load_item.setBrush(QBrush(QColor("red")))
        load_item.setPos(bus1_item.pos().x() - 40, bus1_item.pos().y())
        load_item.setToolTip(load.name)
        load_item.setAcceptHoverEvents(True)
        self.scene.addItem(load_item)
        load.graphics_item = load_item



# Run GUI
# ----------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = NetworkViewer()
    view.resize(500, 400)
    view.show()
    sys.exit(app.exec())

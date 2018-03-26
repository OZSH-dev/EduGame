import sys
from settings import *

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget

from controllers.field import Field


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.mouse_events = set()

    def init_ui(self):
        self.setWindowTitle(WINDOW_NAME)
        self.set_background_color(Qt.gray)
        self.setFixedSize(800, 500)
        self.center()
        self.show()
        self.start_game()

    def start_game(self):
        self.game_field = Field(800, 500, self)
        self.init_game_timer(self.game_field.tick)

    def restart_game(self):
        self.game_field = Field(800, 500, self, self.game_field)
        self.timer.stop()
        self.init_game_timer(self.game_field.tick)

    def init_game_timer(self, target_method):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(target_method)
        self.timer.start(2)

    def set_background_color(self, color):
        pal = self.palette()
        pal.setColor(self.backgroundRole(), color)
        self.setPalette(pal)
        self.autoFillBackground()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

        if event.key() == Qt.Key_Space:
            self.game_field.dinosaur.entity_logic_object.jump()


if __name__ == '__main__':

    application = QApplication(sys.argv)
    application.setWindowIcon(QtGui.QIcon("assets/icon.png"))
    start = MainWindow()
    sys.exit(application.exec_())
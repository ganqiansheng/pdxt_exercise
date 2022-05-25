import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import *


class QWaitingArrow(QWidget):
    def __init__(self, direction,current_page_No,show_up_icon,show_down_icon, parent=None):
        super(QWaitingArrow, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setObjectName('QWaitingArrow' + direction)
        self.resize(50,50)
        self.current_page_No = current_page_No
        point_w = self.parent().geometry().width()
        point_h = self.parent().geometry().height()
        new_x, new_y = self.repoint(direction, point_w, point_h)
        self.setGeometry(new_x, new_y, 50, 50)
        self.pics = {'left': 'left.png', 'up': 'up.png', 'right': 'right.png', 'down': 'down.png'}
        self.url_pic = '.' + os.sep + 'images' + os.sep + self.pics[direction]
        self.mask_pic = '.' + os.sep + 'images' + os.sep + 'mask.png'
        self.pix = QPixmap(self.mask_pic).scaledToWidth(self.width())
        self.setMask(self.pix.mask())
        self.setWindowOpacity(0.5)
        self.setAttribute(Qt.WA_DeleteOnClose)
        # self.isActiveWindow()


    def repoint(self, direction, point_w, point_h):
        if direction == 'left':
            new_x = 0
            new_y = (point_h - self.height()) // 2
        elif direction == 'up':
            new_x = (point_w - self.width()) // 2
            new_y = 0
        elif direction == 'right':
            new_x = point_w - self.width()
            new_y = (point_h - self.height()) // 2
        else:
            new_x = (point_w - self.width()) // 2
            new_y = point_h - self.height()
        return new_x, new_y

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), QPixmap(self.url_pic))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    wait = QWaitingArrow()
    wait.show()
    sys.exit(app.exec())

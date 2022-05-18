import sys,os
from PyQt5.QtWidgets import *
from mainwidow import *
import qdarkstyle
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMyMainWindow()
    main_window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    main_window.show()
    sys.exit(app.exec())
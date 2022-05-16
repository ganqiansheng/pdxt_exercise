import sys,os
from PyQt5.QtWidgets import *
from mainwidow import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMyMainWindow()
    main_window.show()
    sys.exit(app.exec())
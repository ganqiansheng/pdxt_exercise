import os

from call_client_socket import *
from call_command import *
from login import *
from mainwindow import *


class QCallLogin(QMainWindow):
    def __init__(self, qSocketServiceClient):
        super(QCallLogin, self).__init__()
        self.ui = Ui_MainWindow_call_login()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.qSocketServiceClient = qSocketServiceClient
        self.ui.lineEdit_username.setPlaceholderText('Please input username')
        self.ui.lineEdit_password.setPlaceholderText('Please input password')
        self.ui.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.bind()

    def bind(self):
        self.ui.pushButton_cancel.clicked.connect(self.closeform)
        self.ui.pushButton_login.clicked.connect(self.login)
        self.qSocketServiceClient.signal_recieve.connect(self.do_signal_recieve)

    def do_signal_recieve(self, command_str):
        command_list = command_str.split('/')
        command = command_list[0]
        if command == I_LOGIN_00001:
            userid = command_list[1]
            username = command_list[2]
            password = command_list[3]
            main_window = QCustomMainWindow(self.qSocketServiceClient, userid, username, password)
            main_window.show()
            self.close()
        elif command == I_LOGIN_00002:
            print('command_str', command_str)
        elif command == I_LOGIN_00003:
            print('command_str', command_str)


    def closeform(self):
        # self.close()
        os._exit(0)

    def login(self):
        if self.ui.lineEdit_username.text().strip() == '':
            QMessageBox.information(self, '提示', '用户名不能为空，请重新输入')
            return
        commond_str = COMMAND_A0010001  + '/' + self.ui.lineEdit_username.text() + '/' + self.ui.lineEdit_password.text()
        self.qSocketServiceClient.send_command(commond_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qSocketServiceClient = QSocketServiceClient()
    mainform = QCallLogin(qSocketServiceClient)
    mainform.show()
    sys.exit(app.exec())

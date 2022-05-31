from PyQt5.QtWidgets import *
from mainform_call_terminal import *
from call_command import *

class QCustomMainWindow(QMainWindow):
    def __init__(self,qSocketServiceClient,userid,username,password):
        super(QCustomMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.qSocketServiceClient = qSocketServiceClient
        self.userid = userid
        self.username = username
        self.password = password
        self.ui.label_username.setText(username)
        self.bind()

    def bind(self):
        self.qSocketServiceClient.signal_recieve.connect(self.do_signal_recieve)
        self.ui.pushButton_call_next.clicked.connect(self.call_next)
    def call_next(self):
        command_str = COMMAND_A0010002 + '/' + self.userid
        print(command_str)
        self.ui.textEdit_sent_information.setText(self.ui.textEdit_sent_information.toPlainText()+'\n'+command_str)
        self.qSocketServiceClient.send_command(command_str)
    def do_signal_recieve(self,command_str):
        print('command_str', command_str)
        self.ui.textEdit_sent_information.setText(self.ui.textEdit_sent_information.toPlainText()+'\n'+command_str)

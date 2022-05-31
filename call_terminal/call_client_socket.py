import socket
import sys
import threading
from call_command import *
from PyQt5.QtCore import *
from time import *


class QSocketServiceClient(QObject):
    signal_recieve = pyqtSignal(str)
    def __init__(self):
        super(QSocketServiceClient, self).__init__()
        # super(QSocketServiceClient, self).__init__()
        self.connect_server()
        print(self.socket.recv(1024))

        socket_r =threading.Thread(target=self.socket_recieve)
        socket_r.start()

    def connect_server(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect(('127.0.0.1', 56986))
            self.signal_recieve.emit(I_CONNECT_00001)
        except socket.error as msg:
            print('socket错误：', msg)
            self.signal_recieve.emit(I_CONNECT_00002)
            # sys.exit(1)
        finally:
            pass
    def send_command(self,command_str):
        self.socket.send(bytes(command_str, 'UTF-8'))

    def socket_recieve(self):
        while True:
            try:
                sleep(0.2)
                command_str = str(self.socket.recv(1024), 'UTF-8')
                if command_str == '':
                    print("\r\nsocket error,do reconnect ")
                    self.signal_recieve.emit(I_CONNECT_00002)
                    sleep(3)
                    self.connect_server()
                else:
                    self.signal_recieve.emit(command_str)
                    print(command_str)
            except:
                print('\r\nother error occur ')
                sleep(3)

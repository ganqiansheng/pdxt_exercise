import socket
import sys
import threading
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QSocketServiceThread(QThread):
    signal_command_str = pyqtSignal(tuple, str)
    def __init__(self):
        super(QSocketServiceThread, self).__init__()
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 防止socket server重启后端口被占用（socket.error: [Errno 98] Address already in use）
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind(('127.0.0.1', 56986))
            self.socket.listen(10)
        except socket.error as msg:
            print(msg)
            sys.exit(1)
        print('Waiting connection...')

    def run(self):
        while True:
            time.sleep(0.1)
            conn, addr = self.socket.accept()
            self.conn = conn
            t = threading.Thread(target=self.deal_data, args=(conn, addr))
            t.start()

    def deal_data(self, conn, addr):
        print('Accept new connection from {0}'.format(addr))
        conn.send(('Hi, Welcome to the server!').encode())
        while True:
            data = conn.recv(1024)
            print('{0} client send data is {1}'.format(addr,data.decode()))
            # b'\xe8\xbf\x99\xe6\xac\xa1\xe5\x8f\xaf\xe4\xbb\xa5\xe4\xba\x86'
            time.sleep(1)
            if data == b'exit' or not data:
                print('{0} connection close'.format(addr))
                conn.send(bytes('Connection closed!', 'UTF-8'))
                break
            # conn.send(bytes('Hello, {0}'.format(data), "UTF-8"))  # TypeError: a bytes-like object is required, not 'str'
            self.signal_command_str.emit(addr,data.decode())
        conn.close()
    def send_command(self,commond_str):
        try:
            self.conn.send(bytes(commond_str, 'UTF-8'))
        except:
            print('异常')
if __name__ == '__main__':
    app = QApplication(sys.argv)

    qSocketServiceThread = QSocketServiceThread()
    qSocketServiceThread.start()

    sys.exit(app.exec())
# # 创建 socket 对象
# serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 获取本地主机名
# host = socket.gethostname()
# port = 9999
# # 绑定端口
# serversocket.bind((host, port))
# # 设置最大连接数，超过后排队
# serversocket.close()
# serversocket.listen(5)
#
# while True:
#     # 建立客户端连接
#     clientsocket, addr = serversocket.accept()
#     print("连接地址: %s" % str(addr))
#     msg = '欢迎访问W3Cschool教程！' + "\r\n"
#     clientsocket.send(msg.encode('utf-8'))
#     clientsocket.close()

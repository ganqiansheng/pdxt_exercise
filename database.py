import pymssql
from PyQt5.QtWidgets import QMessageBox


def server_connect():
    host = '192.168.1.16'
    user = 'sa'
    password = '56986041'
    database = 'pd_sys'

    conn = pymssql.connect(host=host, user=user, password=password, database=database)
    print(conn)
    if not conn:
        QMessageBox.critical('', '错误提示', '数据库打开错误')
        return '',False
    else:
        # QMessageBox.critical(self, '提示', '数据库打开成功')
        return conn,True


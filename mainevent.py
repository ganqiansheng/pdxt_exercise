import database
from call_terminal.call_command import *
from spiders import *


class QMainEvent(QObject):
    signal_information = pyqtSignal(str)
    def __init__(self):
        super(QMainEvent, self).__init__()
        # 设置socket连接
        self.qSocketServiceThread = QSocketServiceThread()
        self.qSocketServiceThread.start()
        self.bind()
        # 设置数据库连接
        self.conn = self.__openTable()

    def bind(self):
        self.qSocketServiceThread.signal_command_str.connect(self.do_with_socket_command)

    def __openTable(self):
        conn, success = database.server_connect()
        if not success:
            QMessageBox.critical(self, '错误提示', '数据库打开错误')
            return
        return conn

    def do_with_socket_command(self, addr, command_str):
        ip = addr[0]
        port = addr[1]
        command_list = command_str.split('/')
        if command_list[0] == COMMAND_A0010001:
            informaiont_string = '登录IP:' + ip + '\n' + '登录指令Command:' + command_str + '\n'
            self.signal_information.emit(informaiont_string)
            self.user_login(command_list[1], command_list[2])
        elif command_list[0] == COMMAND_A0010002:
            informaiont_string = '远程IP' + ip + '顺呼,工号：' + command_list[1] + '\n'
            self.signal_information.emit(informaiont_string)
            self.user_call(command_list[1])

    def user_login(self, userid, password):
        cursor = self.conn.cursor()
        querystr = " SELECT yhid,yhmc,mm from t_yh where hszh = 98 and yhid = '" + userid + "' "
        cursor.execute(querystr)
        user_rows = cursor.fetchall()
        querystr = " SELECT ksid from t_yh_ks where hszh = 98 and yhid = '" + userid + "' "
        cursor.execute(querystr)
        group_rows = cursor.fetchall()
        cursor.close()
        # groupid_list = []
        # for item in group_rows:
        #     groupid_list.append(item[0])
        groupid_list = [item[0] for item in group_rows]
        if len(user_rows) == 0:
            # 没有这个工号
            self.qSocketServiceThread.send_command(I_LOGIN_00003)
            informaiont_string = '登录  userid:' + userid + '  没有这个工号'  + '\n'
            self.signal_information.emit(informaiont_string)
        elif user_rows[0][2] != password:
            #   密码不对
            self.qSocketServiceThread.send_command(I_LOGIN_00002)
            informaiont_string = '登录  userid:' + userid + '  密码不对' + '\n'
            self.signal_information.emit(informaiont_string)
        elif len(group_rows) == 0:
            # 没有设置呼叫科室
            self.qSocketServiceThread.send_command(I_LOGIN_00004)
            informaiont_string = '登录  userid:' + userid + '  没有设置呼叫科室' + '\n'
            self.signal_information.emit(informaiont_string)
        elif len([groupid for groupid in groupid_list if groupid.strip() != '']) == 0:
            # 没有设置呼叫科室
            self.qSocketServiceThread.send_command(I_LOGIN_00004)
            informaiont_string = '登录  userid:' + userid + '  没有设置呼叫科室' + '\n'
            self.signal_information.emit(informaiont_string)

        else:
            username = user_rows[0][1]
            informaiont_string = '登录成功  userid:' + userid + '  username' + username + '\n'
            self.signal_information.emit(informaiont_string)
            cursor = self.conn.cursor()
            querystr = "UPDATE t_HJZD SET YHID = '" + userid + "' WHERE HSZH = 98 and zdid =1"
            cursor.execute(querystr)
            cursor.close()
            #   登录成功
            self.qSocketServiceThread.send_command(I_LOGIN_00001 + '/' + userid + '/' + username + '/' + password)
            informaiont_string = '登录  userid:' + userid + '  登录成功' + '\n'
            self.signal_information.emit(informaiont_string)

    def user_call(self, userid):
        cursor = self.conn.cursor()
        querystr = " SELECT ksid from t_yh_ks where hszh = 98 and yhid = '" + userid + "' "
        cursor.execute(querystr)
        rows = cursor.fetchall()
        cursor.close()

import matplotlib

from call_terminal.call_command import *
from class_staff_setting import *
from classgroupsetting import *
from group_waiting_arrow import *
from groupwaitinginforamtion import *
from mainform import *
from reportform.dayreport import QDayRepotr
from spiders import *
from mainevent import *

class QMyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dir = {1: None, 2: None, 3: None, 4: None}
        self.arrow_identification = {1: 'left', 2: 'up', 3: 'right', 4: 'down'}
        # 一个护士站中最大的科室数量，如果超出此数量则部分科室不会在科室列表界面显示
        self.total_page = 0
        self.max_group_number_every_page = 4
        self.row_col = {0: (0, 0), 1: (1, 1), 2: (1, 2), 4: (2, 2), 6: (2, 3), 9: (3, 3), 16: (4, 4)}
        self.current_page_No = 0
        self.page_up = False
        self.page_down = False
        self.show_up_icon = False
        self.show_down_icon = False
        self.mainevent = QMainEvent()
        self.conn = self.mainevent.conn
        #收到信号后在主界面的信息窗口显示Socket消息的具体内容
        self.mainevent.signal_information.connect(self.show_information)
        # self.pix = QBitmap('.'+ os.sep + 'images' + os.sep + 'mask.png')
        # self.pix.scaledToWidth(self.width())
        # self.setMask(self.pix)
        self.ui.tableView_login_message.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableView_login_message.setSelectionMode(QAbstractItemView.SingleSelection)
        # self.ui.tableView_login_message.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.ui.tableView_login_message.setSelectionMode(QAbstractItemView.SingleSelection)
        # self.ui.tableView_login_message.horizontalHeader().setStretchLastSection(True)
        self.ui.tableView_login_message.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView_login_message.setAlternatingRowColors(True)
        self.ui.tableView_login_message.setStyleSheet(
            "QTableView{background-color: rgb(250, 250, 250);alternate-background-color: rgb(234, 228, 234);}")  # 设置表格颜色

        self.ui.tableView_login_message.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableView_login_message.customContextMenuRequested.connect(self.login_message_generate_menu)
        ###########


        # self.__openTable()
        # 显示窗体左侧的选医生信息窗
        self.set_tableView_login_message()
        # 显示右侧各科室病人等候情况窗
        self.set_group_waiting_inforamtion()

        self.ui.frame_group_queue_information.installEventFilter(self)

    def show_information(self,information_string):
        self.ui.textEdit_information.setPlainText(
            self.ui.textEdit_information.toPlainText() + information_string)
        self.ui.textEdit_information.moveCursor(QTextCursor.End)

    def eventFilter(self, object, event):
        if object is self.ui.frame_group_queue_information:
            if event.type() == QEvent.ToolTip:
                # print('(frame鼠标的当前位置为：',event.pos())
                # print('frame_group_queue_information.geometry',self.ui.frame_group_queue_information.geometry())
                mouse_position = self.get_current_position(event.pos())
        return QWidget.eventFilter(self, object, event)

    def get_current_position(self, point):
        mouse_x = point.x()
        mouse_y = point.y()
        x = self.ui.frame_group_queue_information.geometry().x()
        y = self.ui.frame_group_queue_information.geometry().y()
        width = self.ui.frame_group_queue_information.width()
        height = self.ui.frame_group_queue_information.height()
        # 初始没有方向值
        direction = 0
        # 左

        if mouse_x < 20 and abs(mouse_y - height / 2) < 10:
            print('左')
            direction = 1
            self.deal_with_direction(direction)
            print(self.group_waiting_arrow.objectName())
            return 1
        # 上
        elif mouse_y < 30 and abs(mouse_x - width / 2) < 20:
            print('上')
            direction = 2
            self.deal_with_direction(direction)
            print(self.group_waiting_arrow.objectName())
            return 2
        # 右
        elif (width - mouse_x) < 20 and abs(mouse_y - height / 2) < 10:
            print('右')
            direction = 3
            self.deal_with_direction(direction)
            print(self.group_waiting_arrow.objectName())
            return 3
        # 下
        elif (height - mouse_y) < 20 and abs(mouse_x - width / 2) < 10:
            print('下')
            direction = 4
            self.deal_with_direction(direction)
            print(self.group_waiting_arrow.objectName())
            return 4
        else:
            direction = 0
            self.deal_with_direction(direction)
            return 0

    def deal_with_direction(self, direction):
        if direction != 0:
            if self.dir[direction] is None:
                self.group_waiting_arrow = QWaitingArrow(self.arrow_identification[direction], self.current_page_No,
                                                         self.show_up_icon, self.show_down_icon,
                                                         self.ui.frame_group_queue_information)
        for n in range(1, 5):
            if n == direction:
                self.dir[direction] = self.group_waiting_arrow
                self.group_waiting_arrow.show()
            else:
                if self.dir[n] is not None:
                    self.dir[n].close()
                self.dir[n] = None

    @pyqtSlot()
    def on_action_staff_manage_triggered(self):
        staffsetting = QStaffSetting(self)
        staffsetting.show()

    @pyqtSlot()
    def on_action_report_triggered(self):
        qDayRepotr = QDayRepotr(self.conn)
        qDayRepotr.exec_()

    @pyqtSlot()
    def on_action_group_manage_triggered(self):
        print('on_action_group_manage_triggered')
        groupsetting = QGroupSetting(self)
        groupsetting.show()

    # def paintEvent(self, event):
    #     painter=QPainter(self)
    #     painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),self.pix)
    #

    def set_group_waiting_inforamtion(self):
        '''
        1、查询有病人或者医生登录的科室数量及相关信息，包括科室的名称，已就诊病人，等候病人
        2、根据科室的数量生成对应的窗口数量及位置，位置排列根据之前预设的排序模型来建立
        3、查询每个科室的病人的详细信息，包括：序号、姓名、号码、类型、医生、号别、优先级、挂号时间、预约时间
        '''

        cursor = self.conn.cursor()
        querystr = """
            SELECT a.KSID, b.KSMC,a.count FROM 
                (SELECT count(*)as count,KSID 
                    FROM t_DHXX 
                    WHERE JZBZ =1 GROUP BY KSID) as a,
                    (SELECT KSID,KSMC FROM t_KS) as b 
                    WHERE a.KSID = b.KSID 
        """
        cursor.execute(querystr)
        rows = cursor.fetchall()
        self.total_page = len(rows) // self.max_group_number_every_page
        if len(rows) % self.max_group_number_every_page != 0:
            self.total_page += 1
        print('总页数：', self.total_page)
        print('当前页：', self.current_page_No)
        self.show_icon()
        if len(rows) > self.max_group_number_every_page:
            querystr += " ORDER BY a.ksid offset " + str(
                self.current_page_No * self.max_group_number_every_page) + " rows fetch next " + str(
                self.max_group_number_every_page) + " rows only"
            cursor.execute(querystr)
            rows = cursor.fetchall()

        cursor.close()
        # self.total_page = len(rows) + (0 if )
        for i in range(len(rows)):
            for j in range(len(rows[0])):
                print(rows[i][j])

        group_waiting_information_lists = []
        for i in range(len(rows)):
            group_waiting_information_list = QGroupWaitingInformation(
                'group_waiting_information_list_' + rows[i][1] + '_' + rows[i][0])
            group_waiting_information_lists.append(group_waiting_information_list)
        # for i in range(len(rows)):
        #     group_waiting_information_list = QGroupWaitingInformation()
        #     group_waiting_information_list.setObjectName('group_waiting_information_list_'+ rows[i][1] + '_'+rows[i][0])
        #     group_waiting_information_lists.append(group_waiting_information_list)

        print(len(group_waiting_information_lists))

        grid_group_waiting_information = QGridLayout(self.ui.frame_group_queue_information)
        # 如果科室数量小于设定的显示科室数量最大值，按科室数量显示
        # 如果科室数量大于设定的显示科室数量最大值，按设定的显示科室数量最大值显示
        display_group_number = len(rows)
        row_number = 0
        col_number = 0
        keys = sorted(self.row_col.keys())
        for key in keys:
            if display_group_number <= key:
                row_number = self.row_col[key][0]
                col_number = self.row_col[key][1]
                break

        for i in range(display_group_number):
            row_no = i // col_number
            # if i - i % col_number > 0:
            #     row_no += 1
            col_no = i % col_number

            grid_group_waiting_information.addWidget(group_waiting_information_lists[i], row_no, col_no)
            print(group_waiting_information_lists[i].objectName())

    def show_icon(self):
        if (self.total_page > 1) and (self.current_page_No > 0):
            self.show_up_icon = True
        if (self.total_page > self.current_page_No):
            self.show_down_icon = True
        if self.current_page_No == 0:
            self.show_up_icon = False
        if self.current_page_No == self.total_page:
            self.show_down_icon = False

    def login_message_generate_menu(self, pos):
        print(pos)
        currentRow = self.ui.tableView_login_message.currentIndex().row()
        if currentRow == -1:
            QMessageBox.warning(self, '提示', '没有数据')
            return

        # ii = self.ui.tableView_login_message.selectionModel().selection().indexes()
        # i = ii[0].row()
        doctor_No = self.model.item(currentRow, 2).text()
        room_No = self.model.item(currentRow, 3).text()
        waiting_number = self.model.item(currentRow, 4).text()
        finished_number = self.model.item(currentRow, 5).text()
        print(doctor_No)

        menu = QMenu()
        item1 = menu.addAction('医生姓名:' + doctor_No)
        item2 = menu.addAction('诊室号:' + room_No)
        item3 = menu.addAction('等候人数:' + waiting_number)
        item4 = menu.addAction('已诊人数:' + finished_number)
        menu.addSeparator()
        item5 = menu.addAction('刷新')

        screenpos = self.ui.tableView_login_message.mapToGlobal(pos)
        action = menu.exec_(screenpos)

        if action == item5:
            self.set_tableView_login_message()
        else:
            pass

    def set_tableView_login_message(self):
        cursor = self.conn.cursor()
        querystr = """
            SELECT zdid,c.yhid,yhmc,fjh,waiting_num,d.finished_num from 
                (SELECT zdid,a.yhid,yhmc,fjh,waiting_num FROM 
                        ((SELECT ZDID,t_hjzd.YHID as YHID,YHMC,FJH FROM  t_hjzd
                                        left outer join t_yh on t_hjzd.yhid=t_yh.yhid and t_hjzd.hszh=t_yh.hszh
                                        where t_hjzd.yhid<>'' and t_hjzd.yhid is not null
                                        and t_hjzd.hszh=98  and t_hjzd.zt<>'暂停' ) as a LEFT JOIN  
                                (SELECT count(*) as waiting_num,t_dhxx.yhid as YHID  FROM t_DHXX
                                            WHERE t_DHXX.JZBZ = 1   and t_dhxx.hszh=98 and t_dhxx.yhid <>'' GROUP BY t_dhxx.yhid ) AS b
                                            ON a.yhid = b.yhid)) AS c LEFT JOIN
                                (SELECT count(*) as finished_num,t_dhxx.yhid as yhid     FROM t_DHXX
                                WHERE t_DHXX.JZBZ = 0  and t_dhxx.ztbz<>3  and t_dhxx.hszh=98 
                                GROUP BY t_dhxx.yhid) AS d
                                        ON c.yhid = d.yhid
        """
        cursor.execute(querystr)
        rows = cursor.fetchall()
        cursor.close()

        if len(rows) < 1:
            # QMessageBox.critical(self, '提示', '没有查询到任何数据')
            pass
            return
        # self.ui.tableView_login_message.set
        self.model = QStandardItemModel()
        self.model.setColumnCount(6)
        self.model.setRowCount(len(rows))
        rowlist = ['终端号', '工号', '姓名', '诊室', '候诊', '已诊']
        self.model.setHorizontalHeaderLabels(rowlist)
        self.ui.tableView_login_message.setModel(self.model)
        self.ui.tableView_login_message.setColumnHidden(0, True)
        self.ui.tableView_login_message.setColumnHidden(1, True)

        for i in range(len(rows)):
            for j in range(len(rows[0])):
                if str(rows[i][j]) == 'None':
                    item = QStandardItem('')
                else:
                    item = QStandardItem(str(rows[i][j]))
                self.model.setItem(i, j, item)

        # self.qryModel = QSqlQueryModel(self)
        # querystr = """
        #     SELECT a.ZDID,a.YHID,a.YHMC,a.FJH,b.waiting_num,c.finished_num FROM
        #         (SELECT ZDID,t_hjzd.YHID as YHID,YHMC,FJH FROM  t_hjzd
        #             left outer join t_yh on t_hjzd.yhid=t_yh.yhid and t_hjzd.hszh=t_yh.hszh
        #             where t_hjzd.yhid<>'' and t_hjzd.yhid is not null
        #             and t_hjzd.hszh=98  and t_hjzd.zt<>'暂停') AS a,
        #         (SELECT count(*) as waiting_num,t_dhxx.yhid as YHID  FROM t_DHXX
        #             WHERE t_DHXX.JZBZ = 1   and t_dhxx.hszh=98 GROUP BY t_dhxx.yhid ) AS b,
        #         (SELECT count(*) as finished_num,t_dhxx.yhid as yhid     FROM t_DHXX
        #             WHERE t_DHXX.JZBZ = 0  and t_dhxx.ztbz<>3  and t_dhxx.hszh=98
        #             GROUP BY t_dhxx.yhid) as c
        #     where a.YHID = b.YHID and a.yhid = c.yhid
        # """
        #
        # self.qryModel.setQuery(querystr,self.db)
        # while self.qryModel.canFetchMore():
        #     self.qryModel.fetchMore()
        # # if not self.qryModel.query():
        # #     QMessageBox.information(self, '提示', '数据查询失败！！！！')
        # # else:
        # #     # QMessageBox.information(self, '提示', '数据查询成功！！！！')
        # #     pass
        # if self.qryModel.lastError().isValid():
        #     QMessageBox.critical(self, "错误", "数据表查询错误，出错消息\n" + self.qryModel.lastError().text())
        #     return
        # self.ui.statusbar.showMessage("记录条数：%d" % self.qryModel.rowCount())
        #
        # self.qryModel.setHeaderData(0, Qt.Horizontal, '终端号')
        # self.qryModel.setHeaderData(1, Qt.Horizontal, '工号')
        # self.qryModel.setHeaderData(2, Qt.Horizontal, '姓名')
        # self.qryModel.setHeaderData(3, Qt.Horizontal, '房间')
        # self.qryModel.setHeaderData(4, Qt.Horizontal, '病人数')
        # self.qryModel.setHeaderData(5, Qt.Horizontal, '就诊数')
        #
        #
        #
        # self.ui.tableView_login_message.setColumnHidden(0, True)
        # self.ui.tableView_login_message.setColumnHidden(1, True)
        #
        # myqurey = QSqlQuery()
        # # myqurey.bindValue(0)
        # myqurey.exec(querystr)
        # print(myqurey.record().count())
        # rec = myqurey.record()
        # for i in range(myqurey.record().count()):
        #     print(rec.fieldName(i))
        # while (myqurey.next()):
        #     print(myqurey.value(0))

    def __openTable(self):
        self.conn, success = database.server_connect()
        if not success:
            QMessageBox.critical(self, '错误提示', '数据库打开错误')
            return

        # host = '192.168.1.16'
        # user = 'sa'
        # password = '56986041'
        # database = 'pd_sys'
        #
        # self.conn = pymssql.connect(host=host, user=user, password=password, database=database)
        # print(self.conn)
        # if not self.conn:
        #     QMessageBox.critical(self,'错误提示','数据库打开错误')
        # else:
        #     # QMessageBox.critical(self, '提示', '数据库打开成功')
        #     pass

        # print(QSqlDatabase.drivers())
        # self.db = QSqlDatabase.addDatabase('QODBC')
        # # dsn = "Driver={sql server};server=192.168.1.16;database=pd_sys;uid=sa;pwd=56986041"
        # # self.db.setDatabaseName(dsn)
        # self.db.setHostName('192.168.1.16')
        # self.db.setPort(1433)
        # self.db.setDatabaseName('sqltest')
        # self.db.setUserName('sa')
        # self.db.setPassword('56986041')
        #
        # if not self.db.open():
        #     QMessageBox.critical(self, '错误提示', '数据库打开错误\n' + self.db.lastError().text())
        # else:
        #     # QMessageBox.critical(self, '提示', '数据库打开成功')
        #     pass
        #
        # querystr = """
        #     SELECT a.ZDID,a.YHID,a.YHMC,a.FJH,b.waiting_num,c.finished_num FROM
        #         (SELECT ZDID,t_hjzd.YHID as YHID,YHMC,FJH FROM  t_hjzd
        #             left outer join t_yh on t_hjzd.yhid=t_yh.yhid and t_hjzd.hszh=t_yh.hszh
        #             where t_hjzd.yhid<>'' and t_hjzd.yhid is not null
        #             and t_hjzd.hszh=98  and t_hjzd.zt<>'暂停') AS a,
        #         (SELECT count(*) as waiting_num,t_dhxx.yhid as YHID  FROM t_DHXX
        #             WHERE t_DHXX.JZBZ = 1   and t_dhxx.hszh=98 GROUP BY t_dhxx.yhid ) AS b,
        #         (SELECT count(*) as finished_num,t_dhxx.yhid as yhid     FROM t_DHXX
        #             WHERE t_DHXX.JZBZ = 0  and t_dhxx.ztbz<>3  and t_dhxx.hszh=98
        #             GROUP BY t_dhxx.yhid) as c
        #     where a.YHID = b.YHID and a.yhid = c.yhid
        # """
        #
        # a = self.db.exec_(querystr)
        # print(a)
        # while(a.next()):
        #     print(a.value(0))
        #
        # # self.init_tableView_login_message()
        # self.qryModel = QSqlQueryModel(self)
        # querystr = """
        #     SELECT a.ZDID,a.YHID,a.YHMC,a.FJH,b.waiting_num,c.finished_num FROM
        #         (SELECT ZDID,t_hjzd.YHID as YHID,YHMC,FJH FROM  t_hjzd
        #             left outer join t_yh on t_hjzd.yhid=t_yh.yhid and t_hjzd.hszh=t_yh.hszh
        #             where t_hjzd.yhid<>'' and t_hjzd.yhid is not null
        #             and t_hjzd.hszh=98  and t_hjzd.zt<>'暂停') AS a,
        #         (SELECT count(*) as waiting_num,t_dhxx.yhid as YHID  FROM t_DHXX
        #             WHERE t_DHXX.JZBZ = 1   and t_dhxx.hszh=98 GROUP BY t_dhxx.yhid ) AS b,
        #         (SELECT count(*) as finished_num,t_dhxx.yhid as yhid     FROM t_DHXX
        #             WHERE t_DHXX.JZBZ = 0  and t_dhxx.ztbz<>3  and t_dhxx.hszh=98
        #             GROUP BY t_dhxx.yhid) as c
        #     where a.YHID = b.YHID and a.yhid = c.yhid
        # """
        #
        # self.qryModel.setQuery(querystr,self.db)
        # while self.qryModel.canFetchMore():
        #     self.qryModel.fetchMore()
        # # if not self.qryModel.query():
        # #     QMessageBox.information(self, '提示', '数据查询失败！！！！')
        # # else:
        # #     # QMessageBox.information(self, '提示', '数据查询成功！！！！')
        # #     pass
        # if self.qryModel.lastError().isValid():
        #     QMessageBox.critical(self, "错误", "数据表查询错误，出错消息\n" + self.qryModel.lastError().text())
        #     return
        # self.ui.statusbar.showMessage("记录条数：%d" % self.qryModel.rowCount())
        #
        # self.qryModel.setHeaderData(0, Qt.Horizontal, '终端号')
        # self.qryModel.setHeaderData(1, Qt.Horizontal, '工号')
        # self.qryModel.setHeaderData(2, Qt.Horizontal, '姓名')
        # self.qryModel.setHeaderData(3, Qt.Horizontal, '房间')
        # self.qryModel.setHeaderData(4, Qt.Horizontal, '病人数')
        # self.qryModel.setHeaderData(5, Qt.Horizontal, '就诊数')
        #
        # self.ui.tableView_login_message.setModel(self.qryModel)
        # self.ui.tableView_login_message.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.ui.tableView_login_message.setSelectionMode(QAbstractItemView.SingleSelection)
        # self.ui.tableView_login_message.setAlternatingRowColors(True)
        # self.ui.tableView_login_message.setStyleSheet(
        #     "QTableView{background-color: rgb(250, 250, 250);alternate-background-color: rgb(234, 234, 234);}")  # 设置表格颜色
        #
        # self.ui.tableView_login_message.setColumnHidden(0, True)
        # self.ui.tableView_login_message.setColumnHidden(1, True)
        #
        # myqurey = QSqlQuery()
        # # myqurey.bindValue(0)
        # myqurey.exec(querystr)
        # print(myqurey.record().count())
        # rec = myqurey.record()
        # for i in range(myqurey.record().count()):
        #     print(rec.fieldName(i))
        # while (myqurey.next()):
        #     print(myqurey.value(0))

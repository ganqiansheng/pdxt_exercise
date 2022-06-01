from class_staff_setting import *
from classgroupsetting import *
from groupwaitinginforamtion import *
from mainform import *


class QMyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 一个护士站中最大的科室数量，如果超出此数量则部分科室不会在科室列表界面显示
        self.max_group_number_every_page = 6

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
        # 设置数据库连接
        self.__openTable()
        # 显示窗体左侧的选医生信息窗
        self.set_tableView_login_message()
        # 显示右侧各科室病人等候情况窗
        self.set_group_waiting_inforamtion()

    @pyqtSlot()
    def on_action_staff_manage_triggered(self):
        staffsetting = QStaffSetting(self)
        staffsetting.show()

    @pyqtSlot()
    def on_action_group_manage_triggered(self):
        # print('on_action_group_manage_triggered')
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
        cursor.close()
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

        # print(len(group_waiting_information_lists))

        grid_group_waiting_information = QGridLayout(self.ui.frame_group_queue_information)
        # 如果科室数量小于设定的显示科室数量最大值，按科室数量显示
        # 如果科室数量大于设定的显示科室数量最大值，按设定的显示科室数量最大值显示
        display_group_number = len(group_waiting_information_lists) if len(
            group_waiting_information_lists) < self.max_group_number_every_page else self.max_group_number_every_page
        for i in range(display_group_number):
            row_no = i // (display_group_number // 2 + display_group_number % 2)
            col_no = i % (display_group_number // 2 + display_group_number % 2)
            grid_group_waiting_information.addWidget(group_waiting_information_lists[i], row_no, col_no)
            # print(group_waiting_information_lists[i].objectName())
            # group_id = group_waiting_information_lists[i].objectName().split('_')[-1]
            # group_name = group_waiting_information_lists[i].objectName().split('_')[-2]
            #
            # print(group_id)
            #
            # cursor = self.conn.cursor()
            # # querystr = "SELECT kssxid,brxm,ghhm,b.ztmc,c.yhmc FROM (SELECT kssxid,brxm,ghhm,ztbz,yhid FROM t_DHXX WHERE ksid = '" + group_id + "'and jzbz = 1) a,t_jzzt b,t_yh c WHERE a.ztbz = b.ztbz and a.yhid=c.yhid order by kssxid"
            # querystr = """
            #             SELECT kssxid, brxm, ghhm, c.ztmc,  CASE WHEN  y.yhmc  IS NOT NULL THEN y.yhmc  else '' END yhmc  FROM(
            #                 (SELECT kssxid, brxm, ghhm, b.ztmc, yhid FROM
            #                     (SELECT kssxid, brxm, ghhm, ztbz, yhid FROM t_DHXX WHERE ksid = '""" + group_id + """' and jzbz = 1) a, t_jzzt b WHERE a.ztbz = b.ztbz ) AS c
            #                     LEFT JOIN t_yh y ON c.yhid = y.yhid)
            #             ORDER BY kssxid
            #         """
            #
            # cursor.execute(querystr)
            # group_waiting_list = cursor.fetchall()
            # cursor.close()
            #
            # group_waiting_information_lists[i].ui.label_group.setText(group_name)
            # # group_waiting_information_lists[i].ui.tableWidget_group_waiting_information.setModel(group_waiting_model)
            #
            # group_waiting_information_lists[i].ui.tableWidget_group_waiting_information.setRowCount(len(group_waiting_list))
            # group_waiting_information_lists[i].ui.tableWidget_group_waiting_information.setColumnCount(len(group_waiting_list[0]))
            # horizontalHeadLabels = ['序号','姓名','号码','类型','医生']
            # group_waiting_information_lists[i].ui.tableWidget_group_waiting_information.setHorizontalHeaderLabels(horizontalHeadLabels)
            #
            #
            # for ii in range(len(group_waiting_list)):
            #     for jj in range(len(group_waiting_list[0])):
            #         item = QTableWidgetItem(str(group_waiting_list[ii][jj]))
            #         group_waiting_information_lists[i].ui.tableWidget_group_waiting_information.setItem(ii,jj,item)
            #
            # cursor = self.conn.cursor()
            # querystr = "SELECT count(*) AS waiting_number FROM t_DHXX WHERE ksid = '" + group_id + "'and jzbz = 1 group by ksid"
            # cursor.execute(querystr)
            # waiting_number = cursor.fetchall()[0][0]
            #
            # querystr = "SELECT count(*) as waiting_number FROM t_DHXX WHERE ksid = '" + group_id + "' group by ksid"
            # cursor.execute(querystr)
            # patient_number = cursor.fetchall()[0][0]
            # cursor.close()
            # group_waiting_information_lists[i].ui.label_queue_information.setText(str(waiting_number) + '人/' + str(patient_number) + '人')
            #
            # group_waiting_information_lists[i].ui.tableWidget_group_waiting_information.customContextMenuRequested.connect(self.group_waiting_information_generate_menu)

    # def group_waiting_information_generate_menu(self,pos):
    #     print(pos)

    def login_message_generate_menu(self, pos):
        # print(pos)
        currentRow = self.ui.tableView_login_message.currentIndex().row()
        if currentRow == -1:
            QMessageBox.warning(self, '提示', '没有数据')

        # ii = self.ui.tableView_login_message.selectionModel().selection().indexes()
        # i = ii[0].row()
        doctor_No = self.model.item(currentRow, 2).text()
        room_No = self.model.item(currentRow, 3).text()
        waiting_number = self.model.item(currentRow, 4).text()
        finished_number = self.model.item(currentRow, 5).text()
        # print(doctor_No)

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
            SELECT a.ZDID,a.YHID,a.YHMC,a.FJH,b.waiting_num,c.finished_num FROM
                (SELECT ZDID,t_hjzd.YHID as YHID,YHMC,FJH FROM  t_hjzd
                    left outer join t_yh on t_hjzd.yhid=t_yh.yhid and t_hjzd.hszh=t_yh.hszh
                    where t_hjzd.yhid<>'' and t_hjzd.yhid is not null
                    and t_hjzd.hszh=98  and t_hjzd.zt<>'暂停') AS a,
                (SELECT count(*) as waiting_num,t_dhxx.yhid as YHID  FROM t_DHXX
                    WHERE t_DHXX.JZBZ = 1   and t_dhxx.hszh=98 GROUP BY t_dhxx.yhid ) AS b,
                (SELECT count(*) as finished_num,t_dhxx.yhid as yhid     FROM t_DHXX
                    WHERE t_DHXX.JZBZ = 0  and t_dhxx.ztbz<>3  and t_dhxx.hszh=98
                    GROUP BY t_dhxx.yhid) as c
            where a.YHID = b.YHID and a.yhid = c.yhid
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

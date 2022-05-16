# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groupwaitinginforamtion.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtCore import *
from PyQt5.QtSql import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from form_groupwaitinginforamtion import *
import database


class QGroupWaitingInformation(QWidget):
    update_tooltip_signal = pyqtSignal(object)
    def __init__(self,name,parent=None):
        super(QGroupWaitingInformation, self).__init__(parent)
        self.ui = Ui_Form_group_information()
        self.ui.setupUi(self)
        self.setObjectName(name)
        self.initUi()
        self.bind_event()
        self.show_group_waiting_information()

        self.ui.tabWidget.setStyleSheet(
            "QTabWidget{border: none;}")  # 设置QTabWidget边框


    def show_group_waiting_information(self):
        group_id = self.objectName().split('_')[-1]
        group_name = self.objectName().split('_')[-2]

        self.conn,success = database.server_connect()
        if not success:
            QMessageBox.critical(self, '错误提示', '数据库打开错误')
            return
        cursor = self.conn.cursor()
        querystr = """
                    SELECT kssxid, brxm, ghhm, c.ztmc,  CASE WHEN  y.yhmc  IS NOT NULL THEN y.yhmc  else '' END yhmc  FROM(
                        (SELECT kssxid, brxm, ghhm, b.ztmc, yhid FROM 
                            (SELECT kssxid, brxm, ghhm, ztbz, yhid FROM t_DHXX WHERE ksid = '""" + group_id + """' and jzbz = 1) a, t_jzzt b WHERE a.ztbz = b.ztbz ) AS c
                            LEFT JOIN t_yh y ON c.yhid = y.yhid) 
                    ORDER BY kssxid
                """
        cursor.execute(querystr)
        group_waiting_list = cursor.fetchall()
        cursor.close()


        self.ui.label_group.setText(group_name)

        self.ui.tableWidget_group_waiting_information.setRowCount(len(group_waiting_list))
        self.ui.tableWidget_group_waiting_information.setColumnCount(
            len(group_waiting_list[0]))
        horizontalHeadLabels = ['序号', '姓名', '号码', '类型', '医生']
        self.ui.tableWidget_group_waiting_information.setHorizontalHeaderLabels(
            horizontalHeadLabels)

        for ii in range(len(group_waiting_list)):
            for jj in range(len(group_waiting_list[0])):
                item = QTableWidgetItem(str(group_waiting_list[ii][jj]))
                self.ui.tableWidget_group_waiting_information.setItem(ii, jj, item)

        cursor = self.conn.cursor()
        querystr = "SELECT count(*) AS waiting_number FROM t_DHXX WHERE ksid = '" + group_id + "'and jzbz = 1 group by ksid"
        cursor.execute(querystr)
        waiting_number = cursor.fetchall()[0][0]

        querystr = "SELECT count(*) as waiting_number FROM t_DHXX WHERE ksid = '" + group_id + "' group by ksid"
        cursor.execute(querystr)
        patient_number = cursor.fetchall()[0][0]
        cursor.close()
        self.ui.label_queue_information.setText(
            str(waiting_number) + '人/' + str(patient_number) + '人')



    def bind_event(self):
        self.ui.tableWidget_group_waiting_information.customContextMenuRequested.connect(
            self.group_waiting_information_generate_menu)
        self.update_tooltip_signal.connect(self.update_tooltip_slot)

    def initUi(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        # QTableWidget.resizeColumnsToContents(self.ui.tableWidget_group_waiting_information)
        # self.ui.tableWidget_group_waiting_information.resize
        self.ui.tableWidget_group_waiting_information.setColumnWidth(0,5)
        self.ui.tableWidget_group_waiting_information.setColumnWidth(1,50)
        self.ui.tableWidget_group_waiting_information.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.ui.tableWidget_group_waiting_information.setHorizontalScrollMode(True)
        self.ui.tableWidget_group_waiting_information.resizeColumnsToContents()

        self.ui.tableWidget_group_waiting_information.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget_group_waiting_information.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableWidget_group_waiting_information.setAlternatingRowColors(True)
        self.ui.tableWidget_group_waiting_information.setStyleSheet(
            "QTableView{background-color: rgb(250, 250, 250);alternate-background-color: rgb(234, 230, 234);}")  # 设置表格颜色
        self.ui.tableWidget_group_waiting_information.verticalHeader().setHidden(True)
        self.ui.tableWidget_group_waiting_information.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableWidget_group_waiting_information.setMouseTracking(True)
        """为TableWidget安装事件过滤器(关键)"""
        self.ui.tableWidget_group_waiting_information.installEventFilter(self)

    def group_waiting_information_generate_menu(self, pos):
        print(pos)
        currentRow = self.ui.tableWidget_group_waiting_information.currentIndex().row()
        patient_name = self.ui.tableWidget_group_waiting_information.item(currentRow,1).text()
        queue_No = self.ui.tableWidget_group_waiting_information.item(currentRow,2).text()
        print(patient_name)
        group_waiting_information_menu = QMenu()
        item1 = group_waiting_information_menu.addAction(queue_No + '号：' + patient_name)
        group_waiting_information_menu.addSeparator()
        item2 = group_waiting_information_menu.addAction('选择医生')
        item3 = group_waiting_information_menu.addAction('提前/退后')
        item4 = group_waiting_information_menu.addAction('设置优先级')
        item5 = group_waiting_information_menu.addAction('弃号')
        group_waiting_information_menu.addSeparator()
        item6 = group_waiting_information_menu.addAction('号码激活')
        group_waiting_information_menu.addSeparator()
        item7 = group_waiting_information_menu.addMenu('召回')
        item71 = item7.addAction('直接召回')
        item72 = item7.addAction('保留医生')
        item8 = group_waiting_information_menu.addMenu('顺序呼叫')
        item81 = item8.addAction('需要呼叫的人数')
        item8.addSeparator()
        item82 = item8.addAction('1人')
        item83 = item8.addAction('2人')
        item84 = item8.addAction('3人')
        item85 = item8.addAction('4人')
        item86 = item8.addAction('5人')
        item87 = item8.addAction('10人')
        item88 = item8.addAction('20人')
        item9 = group_waiting_information_menu.addAction('选择呼叫')
        group_waiting_information_menu.addSeparator()
        group_waiting_information_menu.addAction('手动分诊')
        group_waiting_information_menu.addAction('其他功能')

        screen_pos = self.ui.tableWidget_group_waiting_information.mapToGlobal(pos)
        group_waiting_information_menu.exec_(screen_pos)

    # 通过计算坐标确定当前位置所属单元格
    def update_tooltip_slot(self,pos):
        self.mouse_x = pos.x()
        self.mouse_y = pos.y()
        self.tool_tip = ''
        row_height = 0
        col_width = 0
        for i in range(self.ui.tableWidget_group_waiting_information.rowCount()):
            currentRow_height = self.ui.tableWidget_group_waiting_information.rowHeight(i)
            if i == 0:
                pass
            else:
                if row_height <= self.mouse_y < row_height + currentRow_height:
                    currentRow = i-1
                    print('当前停留行：', currentRow)
                    serial_no = self.ui.tableWidget_group_waiting_information.item(currentRow, 0).text()
                    patient_name = self.ui.tableWidget_group_waiting_information.item(currentRow, 1).text()
                    queue_no = self.ui.tableWidget_group_waiting_information.item(currentRow, 2).text()
                    queue_category = self.ui.tableWidget_group_waiting_information.item(currentRow, 3).text()
                    choosed_doctor = self.ui.tableWidget_group_waiting_information.item(currentRow,4).text() if self.ui.tableWidget_group_waiting_information.item(currentRow, 4).text() != '' else '没选医生'
                    self.tool_tip = '就诊序号：' + serial_no + '\n' + \
                                    '病人姓名：' + patient_name + '\n' + \
                                    '排队号码：' + queue_no + '\n' + \
                                    '就诊类型：' + queue_category + '\n' + \
                                    '选择医生：' + choosed_doctor
                    break
            row_height = row_height + currentRow_height


    def eventFilter(self,object,event):
        if object is self.ui.tableWidget_group_waiting_information:
            self.setCursor(Qt.OpenHandCursor)
            if event.type() == QEvent.ToolTip:
                print('鼠标的当前位置为：',event.pos())
                self.update_tooltip_signal.emit(event.pos())
                # 设置提示气泡显示范围矩形框
                # QRect(x,y,width,height)
                rect = QRect(self.mouse_x, self.mouse_y, 30, 10)
                # 设置QSS样式
                self.ui.tableWidget_group_waiting_information.setStyleSheet(
                    """QToolTip{border:10px;
                       border-top-left-radius:5px;
                       border-top-right-radius:5px;
                       border-bottom-left-radius:5px;
                       border-bottom-right-radius:5px;
                       background:#EAE4EA;
                       color:#AF00AF;
                       font-size:12px;
                       font-family:"微软雅黑";
                    }""")
                QApplication.processEvents()
                QToolTip.showText(QCursor.pos(),self.tool_tip,self.ui.tableWidget_group_waiting_information,rect,3000)
                """
                               showText(QPoint, str, QWidget, QRect, int)
                               #############参数详解###########
                               #QPoint指定tooptip显示的绝对坐标,QCursor.pos()返回当前鼠标所在位置
                               #str为设定的tooptip
                               #QWidget为要展示tooltip的控件
                               #QRect指定tooltip显示的矩形框范围,当鼠标移出该范围,tooltip将隐藏,使用该参数必须指定Qwidget!
                               #int用于指定tooltip显示的时长(毫秒)
                               """

        return QWidget.eventFilter(self,object,event)







from PyQt5.QtCore import *
from PyQt5.QtSql import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import database
from groupsetting import *
from class_staff_detail_setting import *

class QStaffSetting(QMainWindow):
    def __init__(self,parent=None):
        super(QStaffSetting, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUi()
        self.bind_event()
        self.showdata()
        self.conn.close()
    def showdata(self):
        self.conn,result = database.server_connect()
        cursor = self.conn.cursor()
        querystr = "SELECT yhid,yhmc,'' as '科室1','' as '科室2','' as '科室3',rsxe,hjfs,hjrs from t_yh"
        cursor.execute(querystr)
        staff_rows = cursor.fetchall()
        # cursor.close()

        self.ui.tableWidget.setRowCount(len(staff_rows))
        self.ui.tableWidget.setColumnCount(len(staff_rows[0]))

        horizontalHeadLabels = ['工号', '姓名', '科室1', '科室2', '科室3','人数限额','呼叫方式','呼叫人数']
        self.ui.tableWidget.setHorizontalHeaderLabels(
            horizontalHeadLabels)
        for i in range(len(staff_rows)):
            for j in range(len(staff_rows[0])):
                item = QTableWidgetItem(str(staff_rows[i][j]))
                self.ui.tableWidget.setItem(i,j,item)
            #这是一个临时的做法，t_yh_ks表中的医生cxfyi的科室的前三个（如果有的话），单独赋值给tabwidget中科室对应的列，优化做法是优先查询语句
            querystr = "SELECT yhid,ksmc FROM (SELECT yhid,ksid,seq FROM t_yh_ks WHERE yhid = '"+ staff_rows[i][0] +"' AND ksid <>'' ) AS a,t_ks b WHERE a.KSID = b.KSID order by seq"
            cursor.execute(querystr)
            group_rows = cursor.fetchall()
            if len(group_rows) > 3 :
                bound = 3
            else:
                bound = len(group_rows)
            for j in range(2,2+bound):
                item = QTableWidgetItem(str(group_rows[j-2][1]))
                self.ui.tableWidget.setItem(i, j, item)

    def bind_event(self):
        self.ui.tableWidget.itemDoubleClicked.connect(self.doubleClickTableWidget)
    def doubleClickTableWidget(self):
        self.on_action_open_triggered()

    def initUi(self):
        self.setWindowTitle('医生设置')
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.setAlternatingRowColors(True)
        self.ui.tableWidget.setStyleSheet(
            "QTableView{background-color: rgb(250, 250, 250);alternate-background-color: rgb(234, 230, 234);}")  # 设置表格颜色
        self.ui.tableWidget.verticalHeader().setHidden(True)
        self.ui.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)

    @pyqtSlot()
    def on_action_open_triggered(self):
        currentRow = self.ui.tableWidget.currentIndex().row()
        current_yhid = self.ui.tableWidget.item(currentRow,0).text()

        staffDetailSetting = QStaffDetailSetting(current_yhid)
        staffDetailSetting.exec()
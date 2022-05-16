from PyQt5.QtCore import *
from PyQt5.QtSql import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import database
from groupsetting import *
from classgroupdetailsetting import *

class QGroupSetting(QMainWindow):
    def __init__(self,parent=None):
        super(QGroupSetting, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUi()
        self.bind_event()

        self.conn,result = database.server_connect()
        cursor = self.conn.cursor()
        querystr = """
                        SELECT ksid,ksmc,dqhm,qshm,zdhm,
                                CASE WHEN kfbz=1 then '无效' ELSE '有效' END kfbz,
                                CASE WHEN hmpx=1 then '是' ELSE '否' END hmpx,hmqz,yyms,
                                CASE WHEN readdelay=0 then '不延时' ELSE CASE WHEN readdelay <59 THEN STUFF('秒', 1, 0, convert(varCHAR(5),readdelay)) ELSE STUFF('分钟', 1, 0, convert(varCHAR(5),readdelay / 60 )) END END readdelay,
                                CASE WHEN seldoctor=0 then '无效' WHEN seldoctor=1 then '选择' ELSE '不选择' END seldoctor,
                                CASE WHEN hided=1 then '隐藏' ELSE '显示' END hided,
                                CASE WHEN needmerge=1 then '是' ELSE '否' END needmerge,
                                CASE WHEN getnewno=1 then '是' ELSE '否' END getnewno from t_ks 
        """
        cursor.execute(querystr)
        group_rows = cursor.fetchall()
        cursor.close()

        self.ui.tableWidget_group.setRowCount(len(group_rows))
        self.ui.tableWidget_group.setColumnCount(len(group_rows[0]))

        horizontalHeadLabels = ['科室代码', '科室名称', '当前号码', '起始号码', '最大号码','状态','重排','前缀','语音','延时','选择医生','隐藏','合并','转入配号']
        self.ui.tableWidget_group.setHorizontalHeaderLabels(
            horizontalHeadLabels)
        for i in range(len(group_rows)):
            for j in range(len(group_rows[0])):
                item = QTableWidgetItem(str(group_rows[i][j]))
                self.ui.tableWidget_group.setItem(i,j,item)
    def bind_event(self):
        self.ui.tableWidget_group.itemDoubleClicked.connect(self.doubleClickTableWidget)
    def doubleClickTableWidget(self):
        self.on_action_open_triggered()

    def initUi(self):
        self.ui.tableWidget_group.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget_group.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableWidget_group.setAlternatingRowColors(True)
        self.ui.tableWidget_group.setStyleSheet(
            "QTableView{background-color: rgb(250, 250, 250);alternate-background-color: rgb(234, 230, 234);}")  # 设置表格颜色
        self.ui.tableWidget_group.verticalHeader().setHidden(True)
        self.ui.tableWidget_group.setContextMenuPolicy(Qt.CustomContextMenu)

    @pyqtSlot()
    def on_action_open_triggered(self):
        currentRow = self.ui.tableWidget_group.currentIndex().row()
        current_ksid = self.ui.tableWidget_group.item(currentRow,0).text()

        groupdetailsetting = QGroupDetailSetting(current_ksid)
        groupdetailsetting.exec()
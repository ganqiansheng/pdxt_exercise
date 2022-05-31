from datetime import *
import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib.font_manager import FontProperties

from reportform.form_day_report import *


class QDayRepotr(QDialog):
    def __init__(self, conn, parent=None):
        super(QDayRepotr, self).__init__(parent)
        self.ui = Ui_Dialog_day_report()
        self.ui.setupUi(self)
        self.conn = conn
        self.dict_weekday = {'0': '星期日', '1': '星期一', '2': '星期二', '3': '星期三', '4': '星期四', '5': '星期五', '6': '星期六',
                             '7': '星期日', }

        self.initUi()
        self.bind()

    def initUi(self):
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui.dateEdit_start.setDate(date.today() + timedelta(days=-1))
        self.ui.dateEdit_end.setDate(date.today())
        self.ui.dateEdit_start.setDisplayFormat('yyyy-MM-dd')
        self.ui.dateEdit_end.setDisplayFormat('yyyy-MM-dd')
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.statics_data =[]
        self.get_group()
        self.get_staff()

    def set_tablewidgt(self):
        # 显示行数为两个日期之差 说明：如果要剔除全零行，则行数会变化
        rows = self.ui.dateEdit_start.date().daysTo(self.ui.dateEdit_end.date())
        self.ui.tableWidget.setRowCount(rows)
        labels_list = ['日期', '星期', '初诊人数', '召回人数', '未呼叫人数', '总人数', '员工数', '平均等待时间', '最长等待时间', '平均受理时间', '最长受理时间',
                       '等待<X(%)', '受理<Y(%)']
        self.ui.tableWidget.setColumnCount(len(labels_list))
        self.ui.tableWidget.setHorizontalHeaderLabels(labels_list)
        ksid = self.ui.comboBox_group.currentText().split('.')[0]
        yhid = self.ui.comboBox_staff.currentText().split('.')[0]
        for i in range(rows):
            datestr = (self.ui.dateEdit_start.date().toPyDate() + timedelta(days=i)).strftime('%Y-%m-%d')
            weekday = self.dict_weekday[(self.ui.dateEdit_start.date().toPyDate() + timedelta(days=i)).strftime('%w')]
            wherestr = " and hszh=98 "
            if ksid != '0':
                wherestr = wherestr + " and ksid= + '" + ksid + "'"
            if yhid != '0':
                wherestr = wherestr + " and yhid= + '" + yhid + "'"
            # 总人数
            cursor = self.conn.cursor()
            querystr = "select count(*) as numb from t_jzjl  where ghsj is not null and jzsj is not null and jzbz=0 and datediff(day,jzsj,'" + datestr + "')=0" + wherestr
            cursor.execute(querystr)
            total_number = cursor.fetchall()
            # 初诊人数
            cursor = self.conn.cursor()
            querystr = "select count(*) as num from t_jzjl where (ztbz=1 or ztbz=5  or ztbz=7) and jzbz=0   and datediff(day,jzsj,'" + datestr + "')=0 " + wherestr
            cursor.execute(querystr)
            first_rows = cursor.fetchall()
            # 复诊人数
            cursor = self.conn.cursor()
            querystr = "select count(*) as num from t_jzjl where ztbz=2 and jzbz=0  and datediff(day,jzsj,'" + datestr + "')=0 " + wherestr
            cursor.execute(querystr)
            second_rows = cursor.fetchall()
            # 弃号人数
            cursor = self.conn.cursor()
            querystr = "select count(*) as num from t_jzjl where (jzbz=1 or (ztbz=3 and jzbz=0)) and datediff(day,ghsj,'" + datestr + "')=0 " + wherestr
            cursor.execute(querystr)
            giveup_no_rows = cursor.fetchall()
            giveup_no_number = giveup_no_rows[0][0] if len(giveup_no_rows) > 0 else 0

            # 当天医生上班人数
            cursor = self.conn.cursor()
            querystr = "select distinct YHID from t_jzjl  where yhid is not null  and datediff(day,jzsj,'" + datestr + "')=0 " + wherestr
            cursor.execute(querystr)
            staff_number = len(cursor.fetchall())

            # 平均等待时间
            cursor = self.conn.cursor()
            querystr = "select datediff(minute, ghsj, jzsj) as numb from t_jzjl where ghsj is not null and jzsj is not null  and datediff(day,jzsj,'" + datestr + "')=0" + wherestr
            cursor.execute(querystr)
            avg_waiting_time_rows = cursor.fetchall()
            valid_avg_waiting_time_list = [avg_waiting_time_rows[j][0] for j in range(len(avg_waiting_time_rows)) if
                                           (0 <= avg_waiting_time_rows[j][0] <= 6000)]
            avg_waiting_time = round(np.mean(valid_avg_waiting_time_list)) if len(
                valid_avg_waiting_time_list) > 0 else 0
            # 等待小于基准等待时间病人数百分比
            number_less_than_standard_wait_time_list = [i for i in valid_avg_waiting_time_list if
                                                        i < int(self.ui.lineEdit_standard_wait_time.text())]
            standard_wait_percent = len(number_less_than_standard_wait_time_list) / len(
                valid_avg_waiting_time_list) if len(valid_avg_waiting_time_list) > 0 else -1
            # 最长等待时间
            max_waiting_time = max(valid_avg_waiting_time_list) if len(valid_avg_waiting_time_list) > 0 else 0
            # 平均受理时间
            querystr = "select jzsj, yhid, jzjssj,datediff(minute,jzsj,jzjssj) as curetime  from t_jzjl where  jzsj is not null and jzjssj is not null and datediff(day,jzsj,'" + datestr + "')=0" + wherestr + " order by yhid,jzsj"
            cursor.execute(querystr)
            avg_cure_time_rows = cursor.fetchall()
            # valid_avg_cure_time_list:去除受理时间过短（小于1分钟）和过长（大于60分钟）的数据
            valid_avg_cure_time_list = [avg_cure_time_rows[j][3] for j in range(len(avg_cure_time_rows)) if
                                        (1 <= avg_cure_time_rows[j][3] <= 60)]
            avg_cure_time = round(np.mean(valid_avg_cure_time_list)) if len(valid_avg_cure_time_list) > 0 else 0
            # 最长受理时间
            max_cure_time = max(valid_avg_cure_time_list) if len(valid_avg_cure_time_list) > 0 else 0
            # 受理小于基准等待时间病人数百分比
            number_less_than_standard_cure_time_list = [i for i in valid_avg_cure_time_list if
                                                        i < int(self.ui.lineEdit_standard_wait_time.text())]
            standard_cure_percent = len(number_less_than_standard_cure_time_list) / len(
                valid_avg_cure_time_list) if len(valid_avg_cure_time_list) > 0 else -1

            item = QTableWidgetItem(datestr)
            # 写入日期
            self.ui.tableWidget.setItem(i, 0, item)
            # 写入星期
            item = QTableWidgetItem(weekday)
            self.ui.tableWidget.setItem(i, 1, item)
            # 写入初诊人数
            item = QTableWidgetItem(str(first_rows[0][0]))
            self.ui.tableWidget.setItem(i, 2, item)
            # 写入复诊人数
            item = QTableWidgetItem(str(second_rows[0][0]))
            self.ui.tableWidget.setItem(i, 3, item)
            # 写入弃号人数
            item = QTableWidgetItem(str(giveup_no_number))
            self.ui.tableWidget.setItem(i, 4, item)
            # 写入病人总人数
            item = QTableWidgetItem(str(first_rows[0][0] + second_rows[0][0] + giveup_no_number))
            self.ui.tableWidget.setItem(i, 5, item)
            # 写入员工人数
            item = QTableWidgetItem(str(staff_number))
            self.ui.tableWidget.setItem(i, 6, item)
            # 写入平均等待时间
            item = QTableWidgetItem(str(avg_waiting_time) if avg_waiting_time != 0 else '')
            self.ui.tableWidget.setItem(i, 7, item)
            # 写入最长等待时间
            item = QTableWidgetItem(str(max_waiting_time) if max_waiting_time != 0 else '')
            self.ui.tableWidget.setItem(i, 8, item)
            # 写入平均受理时间
            item = QTableWidgetItem(str(avg_cure_time) if avg_cure_time != 0 else '')
            self.ui.tableWidget.setItem(i, 9, item)
            # 写入最长受理时间
            item = QTableWidgetItem(str(max_cure_time) if max_cure_time != 0 else '')
            self.ui.tableWidget.setItem(i, 10, item)
            # 写入等待小于基准等待时间病人数百分比 standard_wait_percent
            item = QTableWidgetItem('{:.2%}'.format(standard_wait_percent) if standard_wait_percent != -1 else '')
            self.ui.tableWidget.setItem(i, 11, item)
            # 写入等待小于基准受理时间病人数百分比
            item = QTableWidgetItem('{:.2%}'.format(standard_cure_percent) if standard_cure_percent != -1 else '')
            self.ui.tableWidget.setItem(i, 12, item)

        # 把当前统计数据暂存到self.statics_data中
        self.statics_data.clear()
        for i in range(self.ui.tableWidget.rowCount()):
            statics_data_row = []
            for j in range(self.ui.tableWidget.columnCount()):
                statics_data_row.append(self.ui.tableWidget.item(i,j).text())
            self.statics_data.append(statics_data_row)
        self.show_repot_pic()

    def show_repot_pic(self):
        self.list_date = [self.ui.tableWidget.item(i, 0).text() for i in range(self.ui.tableWidget.rowCount())]
        self.list_first_cure = [int(self.ui.tableWidget.item(i, 2).text()) for i in range(self.ui.tableWidget.rowCount())]
        self.list_second_cure = [int(self.ui.tableWidget.item(i, 3).text()) for i in range(self.ui.tableWidget.rowCount())]
        self.list_giveup_cure = [int(self.ui.tableWidget.item(i, 4).text()) for i in range(self.ui.tableWidget.rowCount())]
        self.list_total_cure = [int(self.ui.tableWidget.item(i, 5).text()) for i in range(self.ui.tableWidget.rowCount())]

        print(self.list_date)
        print(self.list_first_cure)


        # plt.figure(figsize=(200,120))
        plt.cla()
        myfont = FontProperties(fname='fonts/SimHei.ttf')

        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  #Microsoft YaHei
        # matplotlib.RcParams['axes.unicode_minus'] = False
        l1, = plt.plot(self.list_date, self.list_first_cure,linewidth=1)
        l2, = plt.plot(self.list_date, self.list_second_cure,linewidth=1)
        l3, = plt.plot(self.list_date, self.list_giveup_cure,linewidth=1)
        l4, = plt.plot(self.list_date, self.list_total_cure,linewidth=1)
        plt.xticks(rotation=-10)
        number_of_intervals = len(self.list_date) // 5 if len(self.list_date) // 5 > 1 else 1
        plt.xticks(self.list_date[::number_of_intervals])
        plt.grid(True)
        plt.grid(linestyle='-.')
        plt.legend(handles=[l1,l2,l3,l4],labels=['初诊人数','召回人数','未呼叫人数','总人数'])
        plt.title(u'工作状况日报比较图',fontsize='14',fontproperties=myfont,color='red')

        # if QFile.exists('reportform' + os.sep + 'report_pic' + os.sep + 'zzzgrbb.png'):
        #     os.remove('reportform' + os.sep + 'report_pic' + os.sep + 'zzzgrbb.png')
        plt.savefig('reportform' + os.sep + 'report_pic' + os.sep + 'zzzgrbb.png')
        # plt.show()
        pix = QPixmap()
        pix.load('reportform' + os.sep + 'report_pic' + os.sep + 'zzzgrbb.png')
        self.ui.label_pic.setPixmap(pix)


    def set_report_image(self):
        plt.plot(self.list_date, self.list_first_cure)
        plt.show()

    def get_group(self):
        self.ui.comboBox_group.addItem('0.所有科室')
        cursor = self.conn.cursor()
        querystr = "select ksid,ksmc from t_ks where hszh=98"
        cursor.execute(querystr)
        group_rows = cursor.fetchall()
        cursor.close()
        group_list = [group[0] + '.' + group[1] for group in group_rows]
        self.ui.comboBox_group.addItems(group_list)

    def get_staff(self):
        self.ui.comboBox_staff.addItem('0.所有医生')
        cursor = self.conn.cursor()
        querystr = "select yhid,yhmc from t_yh where hszh=98 and qxid = 3"
        cursor.execute(querystr)
        staff_rows = cursor.fetchall()
        cursor.close()
        staff_list = [staff[0] + '.' + staff[1] for staff in staff_rows]
        self.ui.comboBox_staff.addItems(staff_list)

    def dateEdit_start_dateChanged(self):
        self.ui.dateEdit_end.setMinimumDate(self.ui.dateEdit_start.date())

    def dateEdit_end_dateChanged(self):
        self.ui.dateEdit_start.setMaximumDate(self.ui.dateEdit_end.date())

    def del_all_zero_row(self):
        if self.ui.checkBox_del_all_zero_row.checkState() == Qt.Checked:
            count_row = 0
            for i in range(self.ui.tableWidget.rowCount()):
                if self.ui.tableWidget.item(i-count_row,5).text() == '0':
                    self.ui.tableWidget.removeRow(i-count_row)
                    count_row += 1
        else:
            if len(self.statics_data) == 0:
                return
            else:
                self.ui.tableWidget.setRowCount(len(self.statics_data))
                self.ui.tableWidget.setColumnCount(len(self.statics_data[0]))
                for i in range(len(self.statics_data)):
                    for j in range(len(self.statics_data[0])):
                        item = QTableWidgetItem(self.statics_data[i][j])
                        self.ui.tableWidget.setItem(i,j,item)

    def statics(self):
        self.set_tablewidgt()
        if self.ui.checkBox_del_all_zero_row.checkState() == Qt.Checked:
            self.del_all_zero_row()
    def bind(self):
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.dateEdit_start.dateChanged.connect(self.dateEdit_start_dateChanged)
        self.ui.dateEdit_end.dateChanged.connect(self.dateEdit_end_dateChanged)
        self.ui.pushButton_count.clicked.connect(self.statics)
        self.ui.checkBox_del_all_zero_row.stateChanged.connect(self.del_all_zero_row)

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from widget_display_dismode import *
import database

class QDisplayDismode(QWidget):
    def __init__(self,ksid,display_ID,parent=None):
        super(QDisplayDismode, self).__init__(parent)
        self.ui = Ui_Form_display_dismode()
        self.ui.setupUi(self)
        self.ksid = ksid
        self.display_ID = display_ID
        self.setObjectName('DisplayDismode_'+ self.ksid + '_' + str(self.display_ID))
        self.conn, result = database.server_connect()
        self.init_mode()
        self.show_data()
    def show_data(self):
        self.ui.checkBox_display_No.setText(str(self.display_ID) + '号屏')
        cursor = self.conn.cursor()
        querystr = "SELECT xsms FROM t_ks_xszd  WHERE xspid = " + str(self.display_ID) + " and KSID = '" + self.ksid + "'"
        cursor.execute(querystr)
        display_mode_rows = cursor.fetchall()
        cursor.close()
        if len(display_mode_rows) > 0:
            self.ui.checkBox_display_No.setChecked(True)
            display_mode = display_mode_rows[0][0]
            index_display_mode = [i for i in range(self.ui.comboBox_dismode.count()) if self.ui.comboBox_dismode.itemText(i).startswith(str(display_mode))]
            if len(index_display_mode) > 0:
                self.ui.comboBox_dismode.setCurrentIndex(index_display_mode[0])
        # indexes_yyms = [i for i in range(self.ui.comboBox_yyms.count()) if self.ui.comboBox_yyms.itemText(i).startswith(str(group_detail_rows[0][9]))]
        self.conn.close()


    def init_mode(self):
        cursor = self.conn.cursor()
        querystr = "SELECT msid,msmc FROM t_xsms"
        cursor.execute(querystr)
        display_mode_detail_rows = cursor.fetchall()
        cursor.close()
        display_mode_detail_list = []
        for i in range(len(display_mode_detail_rows)):
            display_mode_detail_list.append(str(display_mode_detail_rows[i][0]) + '.' + display_mode_detail_rows[i][1])
        self.ui.comboBox_dismode.addItems(display_mode_detail_list)
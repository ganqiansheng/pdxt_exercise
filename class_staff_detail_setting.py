import os.path

from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import database
from staffdetailsetting import *
import qdarkstyle

class QStaffDetailSetting(QDialog):
    def __init__(self, yhid, parent=None):
        super(QStaffDetailSetting, self).__init__(parent)
        self.ui = Ui_Dialog_staff_detail_setting()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.bind_event()
        self.yhid = yhid
        self.conn, result = database.server_connect()
        self.init_staff_type()
        self.init_group_list()
        self.read_setting_information()


        self.conn.close

    def bind_event(self):
        self.ui.pushButton_exit.clicked.connect(self.close)
        pass
    def init_staff_type(self):
        cursor = self.conn.cursor()
        querystr = "SELECT QXID,QXMC FROM t_QX"
        cursor.execute(querystr)
        qx_datas = cursor.fetchall()
        cursor.close()
        qx_datas_list =[]
        for data in qx_datas:
            qx_datas_list.append(str(data[0]) + '.' + data[1])
        self.ui.comboBox_staff_type.addItems(qx_datas_list)

    def init_group_list(self):
        cursor = self.conn.cursor()
        querystr = "SELECT KSID,KSMC FROM t_KS"
        cursor.execute(querystr)
        ks_datas = cursor.fetchall()
        cursor.close()
        ks_datas_list =[]
        for data in ks_datas:
            ks_datas_list.append(data[0] + '.' + data[1])
        self.ui.comboBox_group.addItems(ks_datas_list)

    def read_setting_information(self):
        cursor = self.conn.cursor()
        selectstr = "SELECT yhid,yhmc,qxid,mm,rsxe,hjfs,hjrs,xl,zc,ptmzsj,zjmzsj,fwzz,tch,zp FROM t_zjxx a INNER JOIN t_yh b on a.dm = b.yhid "
        wherestr = " WHERE yhid ='" + self.yhid + "'"
        querystr = selectstr + wherestr
        cursor.execute(querystr)
        staff_detail_informations = cursor.fetchall()
        cursor.close()
        self.ui.lineEdit_yhid.setText(staff_detail_informations[0][0])
        self.ui.lineEdit_yhmc.setText(staff_detail_informations[0][1])
        #权限
        self.ui.lineEdit_pwd1.setText(staff_detail_informations[0][3])
        self.ui.lineEdit_pwd2.setText(staff_detail_informations[0][3])
        self.ui.lineEdit_max_patient_number.setText(str(staff_detail_informations[0][4]))
        self.ui.lineEdit_call_way.setText(str(staff_detail_informations[0][5]))
        self.ui.lineEdit_called_number.setText(str(staff_detail_informations[0][6]))
        self.ui.lineEdit_education.setText(staff_detail_informations[0][7])
        self.ui.lineEdit_titlename.setText(staff_detail_informations[0][8])
        self.ui.lineEdit_normal_clinic_time.setText(staff_detail_informations[0][9])
        self.ui.lineEdit_pro_clinic_time.setText(staff_detail_informations[0][10])
        self.ui.lineEdit_server_target.setText(staff_detail_informations[0][11])
        self.ui.textEdit_specialist.setPlainText(staff_detail_informations[0][12])
        photo_data = staff_detail_informations[0][13]
        if not photo_data:
            # QMessageBox.warning(self, '提示', '没有照片')
            photo_data = self.get_default_photo()
        pix = QPixmap()
        pix.loadFromData(photo_data)
        w = self.ui.label_doctor_photo.width()
        self.ui.label_doctor_photo.setPixmap(pix.scaledToWidth(w))

    def get_default_photo(self):
        filename = 'mdoctorphoto'
        if not os.path.exists(filename):
            with open(filename,'wb') as f:
                pass

        with open(filename,'rb') as f:
            pic =f.read()
            return pic


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from class_display_dismode import *
import database
from groupdetailset import *


class QGroupDetailSetting(QDialog):
    ###########################################
    #          代码功能说明：
    # 1、这是在科室设置窗口新建或者打开科室而弹出的窗口界面类
    # 2、类传入参数：ksid，根据ksid来获取不同的类的实例的数据
    # 3、操作数据表：t_ks
    # 4、查询语句：SELECT ksid,ksmc,dqhm,qshm,zdhm,CASE WHEN kfbz=1 then '无效' ELSE '有效' END kfbz,CASE WHEN hmpx=1
    #   then '是' ELSE '否' END hmpx,hmqz,yyms,CASE WHEN readdelay=0 then '不延时' ELSE convert(CHAR,readdelay) END
    #   readdelay,CASE WHEN seldoctor=0 then '无效' WHEN seldoctor=1 then '选择' ELSE '不选择' END seldoctor,CASE
    #   WHEN hided=1 then '隐藏' ELSE '显示' END hided,CASE WHEN needmerge=1 then '是' ELSE '否' END needmerge,CASE
    #   WHEN getnewno=1 then '是' ELSE '否' END getnewno from t_ks  where ksid ='1001'
    #

    ###########################################

    # t_ks表中的一个字段ztbz的作用？

    def __init__(self, ksid, parent=None):
        super(QGroupDetailSetting, self).__init__(parent)
        self.ui = Ui_Dialog_group_setting()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.bind_event()
        self.ksid = ksid
        self.conn, result = database.server_connect()
        self.init_sound_mode()
        self.read_setting_information()

    def init_sound_mode(self):
        # 初始化语音模式下拉框
        self.ui.comboBox_yyms.addItem('0.Null')
        cursor = self.conn.cursor()
        querystr = "SELECT msid,msmc FROM t_yyms"
        cursor.execute(querystr)
        sound_mode_detail_rows = cursor.fetchall()
        cursor.close()
        sound_mode_detail_list = []
        for i in range(len(sound_mode_detail_rows)):
            sound_mode_detail_list.append(str(sound_mode_detail_rows[i][0]) + '.' + sound_mode_detail_rows[i][1])
        self.ui.comboBox_yyms.addItems(sound_mode_detail_list)


    def read_setting_information(self):
        cursor = self.conn.cursor()
        selectstr = """
                        SELECT ksid as '0科室代码',
                                ksmc as '1科室名称',
                                dqhm as '2当前号码',
                                qshm as '3起始号码',
                                zdhm as '4最大号码',
                                memo as '5备注',
                                kfbz as '6开放标志',
                                hmpx as '7号码排序',
                                hmqz as '8号码前缀',
                                yyms as '9语音模式',
                                CASE WHEN readdelay=0 then '不延时' ELSE CASE WHEN readdelay <59 THEN STUFF('秒', 1, 0, convert(varCHAR(5),readdelay)) ELSE STUFF('分钟', 1, 0, convert(varCHAR(5),readdelay / 60 )) END END readdelay,
                                seldoctor as '11选择医生',
                                hided as '12主界面隐藏',
                                preparecount as '13准备人数',
                                needmerge as '14合并',
                                getnewno as '15转入配号',
                                yysjdjh as '16预约时间段叫号',
                                yxhj as '17优先呼叫'
                        from t_ks 
                    """
        wherestr = " where ksid ='" + self.ksid + "'"
        querystr = selectstr + wherestr
        cursor.execute(querystr)
        group_detail_rows = cursor.fetchall()
        # cursor.close()

        self.ui.lineEdit_ksid.setText(self.ksid)
        self.ui.lineEdit_ksmc.setText(group_detail_rows[0][1])
        self.ui.lineEdit_dqhm.setText(group_detail_rows[0][2])
        self.ui.lineEdit_qshm.setText(group_detail_rows[0][3])
        self.ui.lineEdit_zdhm.setText(group_detail_rows[0][4])
        self.ui.lineEdit_memo.setText(group_detail_rows[0][5])

        self.ui.radioButton_valid.setChecked(True if group_detail_rows[0][6] == '0' else False)
        self.ui.radioButton_invalid.setChecked(True if group_detail_rows[0][6] == '1' else False)
        self.ui.checkBox_resort.setChecked(True if group_detail_rows[0][7] == 1 else False)
        self.ui.lineEdit_hmqz.setText(group_detail_rows[0][8])
        indexes_yyms = [i for i in range(self.ui.comboBox_yyms.count()) if self.ui.comboBox_yyms.itemText(i).startswith(str(group_detail_rows[0][9]))]
        if not len(indexes_yyms) == 0:
            self.ui.comboBox_yyms.setCurrentIndex(indexes_yyms[0])
        indexes_delay_time = [i for i in range(self.ui.comboBox_delaytime.count()) if self.ui.comboBox_delaytime.itemText(i) == group_detail_rows[0][10]]
        if not len(indexes_delay_time) == 0:
            self.ui.comboBox_delaytime.setCurrentIndex(indexes_delay_time[0])
        self.ui.comboBox_choose_doctor.setCurrentIndex(group_detail_rows[0][11])
        self.ui.checkBox_hide_in_maiform.setChecked(True if group_detail_rows[0][12] == 1 else False)
        if group_detail_rows[0][13] == -1:
            self.ui.comboBox_prepare_number.setCurrentIndex(0)
        else:
            indexes_prepare_number = [i for i in range(self.ui.comboBox_prepare_number.count()) if
                                  self.ui.comboBox_prepare_number.itemText(i) == group_detail_rows[0][13]]
            if not len(indexes_prepare_number) == 0:
                self.ui.comboBox_prepare_number.setCurrentIndex(indexes_prepare_number[0])
        self.ui.checkBox_combine.setChecked(True if group_detail_rows[0][14] == 1 else False)
        self.ui.checkBox_get_no_again.setChecked(True if group_detail_rows[0][15] == 1 else False)
        self.ui.checkBox_appointment_patient_call.setChecked(True if group_detail_rows[0][16] == 1 else False)
        self.ui.checkBox_start_prior_call.setChecked(True if group_detail_rows[0][17] == 1 else False)
        #显示显示屏及显示模式设置区域
        querystr = "select xspid from t_xszd"
        cursor.execute(querystr)
        display_rows = cursor.fetchall()
        cursor.close()
        displaydismodes = []
        for i in range(len(display_rows)):
            display_ID = display_rows[i][0]
            displaydismode = QDisplayDismode(self.ksid,display_ID)
            displaydismodes.append(displaydismode)
        vlayout_displaydismode = QVBoxLayout(self.ui.groupBox_displaydismode)
        for i in range(len(displaydismodes)):
        #     row_display = i // 2
        #     col_display = i % 2
            vlayout_displaydismode.addWidget(displaydismodes[i])
            vlayout_displaydismode.setAlignment(Qt.AlignLeft)


    def bind_event(self):
        self.ui.pushButton_exit.clicked.connect(self.close)

    @pyqtSlot()
    def on_pushButton_save_clicked(self):
        # print('pushButton_save')


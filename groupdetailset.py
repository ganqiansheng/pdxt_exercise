# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groupdetailset.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_group_setting(object):
    def setupUi(self, Dialog_group_setting):
        Dialog_group_setting.setObjectName("Dialog_group_setting")
        Dialog_group_setting.resize(535, 571)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog_group_setting)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog_group_setting)
        self.groupBox_3.setAcceptDrops(False)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 11)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_ksid = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_ksid.setObjectName("lineEdit_ksid")
        self.horizontalLayout.addWidget(self.lineEdit_ksid)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_ksmc = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_ksmc.setObjectName("lineEdit_ksmc")
        self.horizontalLayout_2.addWidget(self.lineEdit_ksmc)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_dqhm = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_dqhm.setEnabled(False)
        self.lineEdit_dqhm.setObjectName("lineEdit_dqhm")
        self.horizontalLayout_3.addWidget(self.lineEdit_dqhm)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_qshm = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_qshm.setEnabled(True)
        self.lineEdit_qshm.setObjectName("lineEdit_qshm")
        self.horizontalLayout_4.addWidget(self.lineEdit_qshm)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_zdhm = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_zdhm.setObjectName("lineEdit_zdhm")
        self.horizontalLayout_5.addWidget(self.lineEdit_zdhm)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit_memo = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_memo.setObjectName("lineEdit_memo")
        self.horizontalLayout_6.addWidget(self.lineEdit_memo)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.comboBox_yyms = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_yyms.setObjectName("comboBox_yyms")
        self.horizontalLayout_7.addWidget(self.comboBox_yyms)
        self.horizontalLayout_7.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.lineEdit_hmqz = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_hmqz.setObjectName("lineEdit_hmqz")
        self.horizontalLayout_8.addWidget(self.lineEdit_hmqz)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_valid = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_valid.setObjectName("radioButton_valid")
        self.gridLayout.addWidget(self.radioButton_valid, 0, 1, 1, 1)
        self.radioButton_invalid = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_invalid.setObjectName("radioButton_invalid")
        self.gridLayout.addWidget(self.radioButton_invalid, 0, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.checkBox_resort = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_resort.setObjectName("checkBox_resort")
        self.verticalLayout.addWidget(self.checkBox_resort)
        self.horizontalLayout_12.addWidget(self.groupBox_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(Dialog_group_setting)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.comboBox_delaytime = QtWidgets.QComboBox(Dialog_group_setting)
        self.comboBox_delaytime.setObjectName("comboBox_delaytime")
        self.comboBox_delaytime.addItem("")
        self.comboBox_delaytime.addItem("")
        self.comboBox_delaytime.addItem("")
        self.comboBox_delaytime.addItem("")
        self.comboBox_delaytime.addItem("")
        self.comboBox_delaytime.addItem("")
        self.comboBox_delaytime.addItem("")
        self.comboBox_delaytime.addItem("")
        self.comboBox_delaytime.addItem("")
        self.comboBox_delaytime.addItem("")
        self.comboBox_delaytime.addItem("")
        self.comboBox_delaytime.addItem("")
        self.comboBox_delaytime.addItem("")
        self.comboBox_delaytime.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_delaytime)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(Dialog_group_setting)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.comboBox_choose_doctor = QtWidgets.QComboBox(Dialog_group_setting)
        self.comboBox_choose_doctor.setObjectName("comboBox_choose_doctor")
        self.comboBox_choose_doctor.addItem("")
        self.comboBox_choose_doctor.addItem("")
        self.comboBox_choose_doctor.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_choose_doctor)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(Dialog_group_setting)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.comboBox_prepare_number = QtWidgets.QComboBox(Dialog_group_setting)
        self.comboBox_prepare_number.setObjectName("comboBox_prepare_number")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.comboBox_prepare_number.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_prepare_number)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.checkBox_get_no_again = QtWidgets.QCheckBox(Dialog_group_setting)
        self.checkBox_get_no_again.setObjectName("checkBox_get_no_again")
        self.verticalLayout_2.addWidget(self.checkBox_get_no_again)
        self.checkBox_hide_in_maiform = QtWidgets.QCheckBox(Dialog_group_setting)
        self.checkBox_hide_in_maiform.setObjectName("checkBox_hide_in_maiform")
        self.verticalLayout_2.addWidget(self.checkBox_hide_in_maiform)
        self.checkBox_combine = QtWidgets.QCheckBox(Dialog_group_setting)
        self.checkBox_combine.setObjectName("checkBox_combine")
        self.verticalLayout_2.addWidget(self.checkBox_combine)
        self.checkBox_start_prior_call = QtWidgets.QCheckBox(Dialog_group_setting)
        self.checkBox_start_prior_call.setObjectName("checkBox_start_prior_call")
        self.verticalLayout_2.addWidget(self.checkBox_start_prior_call)
        self.checkBox_appointment_patient_call = QtWidgets.QCheckBox(Dialog_group_setting)
        self.checkBox_appointment_patient_call.setObjectName("checkBox_appointment_patient_call")
        self.verticalLayout_2.addWidget(self.checkBox_appointment_patient_call)
        self.checkBox_start_sign = QtWidgets.QCheckBox(Dialog_group_setting)
        self.checkBox_start_sign.setObjectName("checkBox_start_sign")
        self.verticalLayout_2.addWidget(self.checkBox_start_sign)
        self.checkBox_start_choose_doctor_while_signing = QtWidgets.QCheckBox(Dialog_group_setting)
        self.checkBox_start_choose_doctor_while_signing.setObjectName("checkBox_start_choose_doctor_while_signing")
        self.verticalLayout_2.addWidget(self.checkBox_start_choose_doctor_while_signing)
        self.horizontalLayout_12.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.groupBox_displaydismode = QtWidgets.QGroupBox(Dialog_group_setting)
        self.groupBox_displaydismode.setObjectName("groupBox_displaydismode")
        self.verticalLayout_3.addWidget(self.groupBox_displaydismode)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem)
        self.pushButton_save = QtWidgets.QPushButton(Dialog_group_setting)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_13.addWidget(self.pushButton_save)
        self.pushButton_exit = QtWidgets.QPushButton(Dialog_group_setting)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/exit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_exit.setIcon(icon1)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout_13.addWidget(self.pushButton_exit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Dialog_group_setting)
        QtCore.QMetaObject.connectSlotsByName(Dialog_group_setting)

    def retranslateUi(self, Dialog_group_setting):
        _translate = QtCore.QCoreApplication.translate
        Dialog_group_setting.setWindowTitle(_translate("Dialog_group_setting", "??????????????????"))
        self.label.setText(_translate("Dialog_group_setting", "???????????????"))
        self.label_2.setText(_translate("Dialog_group_setting", "???????????????"))
        self.label_3.setText(_translate("Dialog_group_setting", "???????????????"))
        self.label_4.setText(_translate("Dialog_group_setting", "???????????????"))
        self.label_5.setText(_translate("Dialog_group_setting", "???????????????"))
        self.label_6.setText(_translate("Dialog_group_setting", "???       ??????"))
        self.label_8.setText(_translate("Dialog_group_setting", "???????????????"))
        self.label_7.setText(_translate("Dialog_group_setting", "???????????????"))
        self.radioButton_valid.setText(_translate("Dialog_group_setting", "??????"))
        self.radioButton_invalid.setText(_translate("Dialog_group_setting", "??????"))
        self.label_12.setText(_translate("Dialog_group_setting", "??????????????????"))
        self.checkBox_resort.setText(_translate("Dialog_group_setting", "?????????????????????"))
        self.label_9.setText(_translate("Dialog_group_setting", "???????????????"))
        self.comboBox_delaytime.setItemText(0, _translate("Dialog_group_setting", "?????????"))
        self.comboBox_delaytime.setItemText(1, _translate("Dialog_group_setting", "10???"))
        self.comboBox_delaytime.setItemText(2, _translate("Dialog_group_setting", "20???"))
        self.comboBox_delaytime.setItemText(3, _translate("Dialog_group_setting", "30???"))
        self.comboBox_delaytime.setItemText(4, _translate("Dialog_group_setting", "1??????"))
        self.comboBox_delaytime.setItemText(5, _translate("Dialog_group_setting", "2??????"))
        self.comboBox_delaytime.setItemText(6, _translate("Dialog_group_setting", "3??????"))
        self.comboBox_delaytime.setItemText(7, _translate("Dialog_group_setting", "4??????"))
        self.comboBox_delaytime.setItemText(8, _translate("Dialog_group_setting", "5??????"))
        self.comboBox_delaytime.setItemText(9, _translate("Dialog_group_setting", "6??????"))
        self.comboBox_delaytime.setItemText(10, _translate("Dialog_group_setting", "7??????"))
        self.comboBox_delaytime.setItemText(11, _translate("Dialog_group_setting", "8??????"))
        self.comboBox_delaytime.setItemText(12, _translate("Dialog_group_setting", "9??????"))
        self.comboBox_delaytime.setItemText(13, _translate("Dialog_group_setting", "10??????"))
        self.label_10.setText(_translate("Dialog_group_setting", "???????????????"))
        self.comboBox_choose_doctor.setItemText(0, _translate("Dialog_group_setting", "0-??????"))
        self.comboBox_choose_doctor.setItemText(1, _translate("Dialog_group_setting", "1-??????"))
        self.comboBox_choose_doctor.setItemText(2, _translate("Dialog_group_setting", "2-??????"))
        self.label_11.setText(_translate("Dialog_group_setting", "???????????????"))
        self.comboBox_prepare_number.setItemText(0, _translate("Dialog_group_setting", "????????????"))
        self.comboBox_prepare_number.setItemText(1, _translate("Dialog_group_setting", "1"))
        self.comboBox_prepare_number.setItemText(2, _translate("Dialog_group_setting", "2"))
        self.comboBox_prepare_number.setItemText(3, _translate("Dialog_group_setting", "3"))
        self.comboBox_prepare_number.setItemText(4, _translate("Dialog_group_setting", "4"))
        self.comboBox_prepare_number.setItemText(5, _translate("Dialog_group_setting", "5"))
        self.comboBox_prepare_number.setItemText(6, _translate("Dialog_group_setting", "6"))
        self.comboBox_prepare_number.setItemText(7, _translate("Dialog_group_setting", "7"))
        self.comboBox_prepare_number.setItemText(8, _translate("Dialog_group_setting", "8"))
        self.comboBox_prepare_number.setItemText(9, _translate("Dialog_group_setting", "9"))
        self.comboBox_prepare_number.setItemText(10, _translate("Dialog_group_setting", "10"))
        self.comboBox_prepare_number.setItemText(11, _translate("Dialog_group_setting", "20"))
        self.comboBox_prepare_number.setItemText(12, _translate("Dialog_group_setting", "30"))
        self.comboBox_prepare_number.setItemText(13, _translate("Dialog_group_setting", "40"))
        self.comboBox_prepare_number.setItemText(14, _translate("Dialog_group_setting", "50"))
        self.comboBox_prepare_number.setItemText(15, _translate("Dialog_group_setting", "60"))
        self.comboBox_prepare_number.setItemText(16, _translate("Dialog_group_setting", "70"))
        self.comboBox_prepare_number.setItemText(17, _translate("Dialog_group_setting", "80"))
        self.comboBox_prepare_number.setItemText(18, _translate("Dialog_group_setting", "90"))
        self.comboBox_prepare_number.setItemText(19, _translate("Dialog_group_setting", "100"))
        self.checkBox_get_no_again.setText(_translate("Dialog_group_setting", "???????????????????????????"))
        self.checkBox_hide_in_maiform.setText(_translate("Dialog_group_setting", "??????????????????"))
        self.checkBox_combine.setText(_translate("Dialog_group_setting", "??????"))
        self.checkBox_start_prior_call.setText(_translate("Dialog_group_setting", "??????????????????"))
        self.checkBox_appointment_patient_call.setText(_translate("Dialog_group_setting", "????????????????????????????????????"))
        self.checkBox_start_sign.setText(_translate("Dialog_group_setting", "??????????????????"))
        self.checkBox_start_choose_doctor_while_signing.setText(_translate("Dialog_group_setting", "?????????????????????"))
        self.groupBox_displaydismode.setTitle(_translate("Dialog_group_setting", "?????????????????????????????????"))
        self.pushButton_save.setText(_translate("Dialog_group_setting", "??????"))
        self.pushButton_exit.setText(_translate("Dialog_group_setting", "??????"))
import res_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groupdetailsetting.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_group_setting(object):
    def setupUi(self, Form_group_setting):
        Form_group_setting.setObjectName("Form_group_setting")
        Form_group_setting.resize(537, 572)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form_group_setting)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.groupBox_3 = QtWidgets.QGroupBox(Form_group_setting)
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
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_5.addWidget(self.lineEdit_5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_6.addWidget(self.lineEdit_6)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_7.addWidget(self.comboBox)
        self.horizontalLayout_7.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_8.addWidget(self.lineEdit_7)
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
        self.label_9 = QtWidgets.QLabel(Form_group_setting)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.comboBox_2 = QtWidgets.QComboBox(Form_group_setting)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_9.addWidget(self.comboBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(Form_group_setting)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.comboBox_3 = QtWidgets.QComboBox(Form_group_setting)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_10.addWidget(self.comboBox_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(Form_group_setting)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.comboBox_4 = QtWidgets.QComboBox(Form_group_setting)
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_11.addWidget(self.comboBox_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.checkBox_get_no_again = QtWidgets.QCheckBox(Form_group_setting)
        self.checkBox_get_no_again.setObjectName("checkBox_get_no_again")
        self.verticalLayout_2.addWidget(self.checkBox_get_no_again)
        self.checkBox_hide_in_maiform = QtWidgets.QCheckBox(Form_group_setting)
        self.checkBox_hide_in_maiform.setObjectName("checkBox_hide_in_maiform")
        self.verticalLayout_2.addWidget(self.checkBox_hide_in_maiform)
        self.checkBox_combine = QtWidgets.QCheckBox(Form_group_setting)
        self.checkBox_combine.setObjectName("checkBox_combine")
        self.verticalLayout_2.addWidget(self.checkBox_combine)
        self.checkBox_start_prior_call = QtWidgets.QCheckBox(Form_group_setting)
        self.checkBox_start_prior_call.setObjectName("checkBox_start_prior_call")
        self.verticalLayout_2.addWidget(self.checkBox_start_prior_call)
        self.checkBox_appointment_patient_call = QtWidgets.QCheckBox(Form_group_setting)
        self.checkBox_appointment_patient_call.setObjectName("checkBox_appointment_patient_call")
        self.verticalLayout_2.addWidget(self.checkBox_appointment_patient_call)
        self.checkBox_start_sign = QtWidgets.QCheckBox(Form_group_setting)
        self.checkBox_start_sign.setObjectName("checkBox_start_sign")
        self.verticalLayout_2.addWidget(self.checkBox_start_sign)
        self.checkBox_start_choose_doctor_while_signing = QtWidgets.QCheckBox(Form_group_setting)
        self.checkBox_start_choose_doctor_while_signing.setObjectName("checkBox_start_choose_doctor_while_signing")
        self.verticalLayout_2.addWidget(self.checkBox_start_choose_doctor_while_signing)
        self.horizontalLayout_12.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.groupBox_2 = QtWidgets.QGroupBox(Form_group_setting)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem)
        self.pushButton_save = QtWidgets.QPushButton(Form_group_setting)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_13.addWidget(self.pushButton_save)
        self.pushButton_exit = QtWidgets.QPushButton(Form_group_setting)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/exit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_exit.setIcon(icon1)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout_13.addWidget(self.pushButton_exit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Form_group_setting)
        QtCore.QMetaObject.connectSlotsByName(Form_group_setting)

    def retranslateUi(self, Form_group_setting):
        _translate = QtCore.QCoreApplication.translate
        Form_group_setting.setWindowTitle(_translate("Form_group_setting", "科室明细设置"))
        self.label.setText(_translate("Form_group_setting", "科室代码："))
        self.label_2.setText(_translate("Form_group_setting", "科室名称："))
        self.label_3.setText(_translate("Form_group_setting", "当前号码："))
        self.label_4.setText(_translate("Form_group_setting", "起始号码："))
        self.label_5.setText(_translate("Form_group_setting", "最大号码："))
        self.label_6.setText(_translate("Form_group_setting", "备       注："))
        self.label_8.setText(_translate("Form_group_setting", "语音模式："))
        self.label_7.setText(_translate("Form_group_setting", "取号前缀："))
        self.radioButton_valid.setText(_translate("Form_group_setting", "有效"))
        self.radioButton_invalid.setText(_translate("Form_group_setting", "无效"))
        self.label_12.setText(_translate("Form_group_setting", "科室有效性："))
        self.checkBox_resort.setText(_translate("Form_group_setting", "按号码重新排序"))
        self.label_9.setText(_translate("Form_group_setting", "读取延时："))
        self.label_10.setText(_translate("Form_group_setting", "选择医生："))
        self.label_11.setText(_translate("Form_group_setting", "准备人数："))
        self.checkBox_get_no_again.setText(_translate("Form_group_setting", "转入时重新分配号码"))
        self.checkBox_hide_in_maiform.setText(_translate("Form_group_setting", "在主界面隐藏"))
        self.checkBox_combine.setText(_translate("Form_group_setting", "合并"))
        self.checkBox_start_prior_call.setText(_translate("Form_group_setting", "开启优先呼叫"))
        self.checkBox_appointment_patient_call.setText(_translate("Form_group_setting", "预约病人到预约时间段叫号"))
        self.checkBox_start_sign.setText(_translate("Form_group_setting", "开启签到功能"))
        self.checkBox_start_choose_doctor_while_signing.setText(_translate("Form_group_setting", "开启签到选医生"))
        self.groupBox_2.setTitle(_translate("Form_group_setting", "显示屏及显示模式设置："))
        self.pushButton_save.setText(_translate("Form_group_setting", "保存"))
        self.pushButton_exit.setText(_translate("Form_group_setting", "退出"))
import groupres_rc
import res_rc
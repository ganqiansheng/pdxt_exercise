# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform_call_terminal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(295, 678)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setObjectName("label_username")
        self.horizontalLayout_5.addWidget(self.label_username)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.label_groupname = QtWidgets.QLabel(self.centralwidget)
        self.label_groupname.setObjectName("label_groupname")
        self.horizontalLayout_4.addWidget(self.label_groupname)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_calling_information = QtWidgets.QLabel(self.centralwidget)
        self.label_calling_information.setObjectName("label_calling_information")
        self.horizontalLayout_3.addWidget(self.label_calling_information)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.textEdit_recieved_information = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_recieved_information.setObjectName("textEdit_recieved_information")
        self.verticalLayout.addWidget(self.textEdit_recieved_information)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.textEdit_sent_information = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_sent_information.setObjectName("textEdit_sent_information")
        self.verticalLayout.addWidget(self.textEdit_sent_information)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_call_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_call_next.setObjectName("pushButton_call_next")
        self.horizontalLayout.addWidget(self.pushButton_call_next)
        self.pushButton_recall = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_recall.setObjectName("pushButton_recall")
        self.horizontalLayout.addWidget(self.pushButton_recall)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_ignore = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ignore.setObjectName("pushButton_ignore")
        self.horizontalLayout_2.addWidget(self.pushButton_ignore)
        self.pushButton_call = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_call.setObjectName("pushButton_call")
        self.horizontalLayout_2.addWidget(self.pushButton_call)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "呼叫终端"))
        self.label.setText(_translate("MainWindow", "医生姓名："))
        self.label_username.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "科室名称："))
        self.label_groupname.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "正在呼叫："))
        self.label_calling_information.setText(_translate("MainWindow", "正在呼叫："))
        self.label_7.setText(_translate("MainWindow", "收到的消息："))
        self.label_8.setText(_translate("MainWindow", "发出的消息："))
        self.pushButton_call_next.setText(_translate("MainWindow", "顺呼"))
        self.pushButton_recall.setText(_translate("MainWindow", "复呼"))
        self.pushButton_ignore.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_call.setText(_translate("MainWindow", "PushButton"))
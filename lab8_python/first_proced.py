# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_proced.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_first_proced(object):
    def setupUi(self, first_proced):
        first_proced.setObjectName("first_proced")
        first_proced.resize(176, 85)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(first_proced.sizePolicy().hasHeightForWidth())
        first_proced.setSizePolicy(sizePolicy)
        self.label = QtWidgets.QLabel(first_proced)
        self.label.setGeometry(QtCore.QRect(0, 0, 91, 16))
        self.label.setObjectName("label")
        self.pushButton_create_report = QtWidgets.QPushButton(first_proced)
        self.pushButton_create_report.setGeometry(QtCore.QRect(50, 30, 93, 28))
        self.pushButton_create_report.setObjectName("pushButton_create_report")
        self.lineEdit = QtWidgets.QLineEdit(first_proced)
        self.lineEdit.setGeometry(QtCore.QRect(90, 0, 51, 22))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(first_proced)
        QtCore.QMetaObject.connectSlotsByName(first_proced)

    def retranslateUi(self, first_proced):
        _translate = QtCore.QCoreApplication.translate
        first_proced.setWindowTitle(_translate("first_proced", "GetTotalCostByContractNumber"))
        self.label.setText(_translate("first_proced", "Enter number:"))
        self.pushButton_create_report.setText(_translate("first_proced", "Create report"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'private_delete.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_private_delete(object):
    def setupUi(self, private_delete):
        private_delete.setObjectName("private_delete")
        private_delete.resize(278, 75)
        self.label = QtWidgets.QLabel(private_delete)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label.setObjectName("label")
        self.pushButton_private_delete = QtWidgets.QPushButton(private_delete)
        self.pushButton_private_delete.setGeometry(QtCore.QRect(100, 40, 93, 28))
        self.pushButton_private_delete.setObjectName("pushButton_private_delete")
        self.lineEdit_private = QtWidgets.QLineEdit(private_delete)
        self.lineEdit_private.setGeometry(QtCore.QRect(160, 10, 113, 22))
        self.lineEdit_private.setObjectName("lineEdit_private")

        self.retranslateUi(private_delete)
        QtCore.QMetaObject.connectSlotsByName(private_delete)

    def retranslateUi(self, private_delete):
        _translate = QtCore.QCoreApplication.translate
        private_delete.setWindowTitle(_translate("private_delete", "Delete private supplier"))
        self.label.setText(_translate("private_delete", "Enter id:"))
        self.pushButton_private_delete.setText(_translate("private_delete", "Delete"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messagebox.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_messagebox(object):
    def setupUi(self, messagebox):
        messagebox.setObjectName("messagebox")
        messagebox.resize(250, 51)
        self.label = QtWidgets.QLabel(messagebox)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(messagebox)
        QtCore.QMetaObject.connectSlotsByName(messagebox)

    def retranslateUi(self, messagebox):
        _translate = QtCore.QCoreApplication.translate
        messagebox.setWindowTitle(_translate("messagebox", "Succes!"))
        self.label.setText(_translate("messagebox", "Changing succesful!"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'errorbox.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_errorbox(object):
    def setupUi(self, errorbox):
        errorbox.setObjectName("errorbox")
        errorbox.resize(250, 51)
        self.label = QtWidgets.QLabel(errorbox)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(errorbox)
        QtCore.QMetaObject.connectSlotsByName(errorbox)

    def retranslateUi(self, errorbox):
        _translate = QtCore.QCoreApplication.translate
        errorbox.setWindowTitle(_translate("errorbox", "Error!"))
        self.label.setText(_translate("errorbox", "Error!"))

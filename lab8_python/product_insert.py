# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'product_insert.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_product_insert(object):
    def setupUi(self, product_insert):
        product_insert.setObjectName("product_insert")
        product_insert.resize(283, 162)
        self.label = QtWidgets.QLabel(product_insert)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(product_insert)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(product_insert)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(product_insert)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 121, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_product_contract = QtWidgets.QLineEdit(product_insert)
        self.lineEdit_product_contract.setGeometry(QtCore.QRect(160, 10, 113, 22))
        self.lineEdit_product_contract.setObjectName("lineEdit_product_contract")
        self.lineEdit_product_name = QtWidgets.QLineEdit(product_insert)
        self.lineEdit_product_name.setGeometry(QtCore.QRect(160, 40, 113, 22))
        self.lineEdit_product_name.setObjectName("lineEdit_product_name")
        self.lineEdit_product_amount = QtWidgets.QLineEdit(product_insert)
        self.lineEdit_product_amount.setGeometry(QtCore.QRect(160, 70, 113, 22))
        self.lineEdit_product_amount.setObjectName("lineEdit_product_amount")
        self.lineEdit_product_price = QtWidgets.QLineEdit(product_insert)
        self.lineEdit_product_price.setGeometry(QtCore.QRect(160, 100, 113, 22))
        self.lineEdit_product_price.setObjectName("lineEdit_product_price")
        self.pushButton_product_insert = QtWidgets.QPushButton(product_insert)
        self.pushButton_product_insert.setGeometry(QtCore.QRect(100, 129, 93, 28))
        self.pushButton_product_insert.setObjectName("pushButton_product_insert")

        self.retranslateUi(product_insert)
        QtCore.QMetaObject.connectSlotsByName(product_insert)

    def retranslateUi(self, product_insert):
        _translate = QtCore.QCoreApplication.translate
        product_insert.setWindowTitle(_translate("product_insert", "Insert to product"))
        self.label.setText(_translate("product_insert", "Enter contract:"))
        self.label_2.setText(_translate("product_insert", "Enter product:"))
        self.label_3.setText(_translate("product_insert", "Enter amount:"))
        self.label_4.setText(_translate("product_insert", "Enter price:"))
        self.pushButton_product_insert.setText(_translate("product_insert", "Insert"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\User\Documents\PROYECT\PharmacyProject\menu\menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(562, 613)
        Dialog.setStyleSheet("background-color: rgb(23, 136, 211)")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 50, 181, 61))
        self.label.setStyleSheet("color: rgb(231, 231, 231);font-size:28pt;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(230, 120, 191, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(230, 160, 171, 61))
        self.pushButton.setStyleSheet("background-color: rgb(167, 168, 167);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 240, 171, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(167, 168, 167);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 320, 171, 61))
        self.pushButton_3.setStyleSheet("background-color: rgb(167, 168, 167);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "PROYECT BY JARED AND MOU "))
        self.pushButton.setText(_translate("Dialog", "ADD PRODUCTS"))
        self.pushButton_2.setText(_translate("Dialog", "CREATE  SALE "))
        self.pushButton_3.setText(_translate("Dialog", "REPORTS "))
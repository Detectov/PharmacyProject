# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\jared\OneDrive\Documentos\OBEJETOS\PharmacyProject\billmenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(620, 480)
        Dialog.setStyleSheet("background-color: rgb(23, 136, 211)")
        self.yesbill = QtWidgets.QPushButton(Dialog)
        self.yesbill.setGeometry(QtCore.QRect(220, 120, 171, 91))
        self.yesbill.setStyleSheet("background-color: rgb(156, 208, 93);\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.yesbill.setObjectName("yesbill")
        self.nobill = QtWidgets.QPushButton(Dialog)
        self.nobill.setGeometry(QtCore.QRect(220, 240, 171, 91))
        self.nobill.setStyleSheet("background-color: rgb(156, 208, 93);\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.nobill.setObjectName("nobill")
        self.backbutt = QtWidgets.QPushButton(Dialog)
        self.backbutt.setGeometry(QtCore.QRect(462, 417, 121, 41))
        self.backbutt.setStyleSheet("background-color: rgb(156, 208, 93);\n"
"color: rgb(255, 255, 255);")
        self.backbutt.setObjectName("backbutt")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 50, 35, 10))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.yesbill.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Billed</span></p></body></html>"))
        self.yesbill.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">Perro</span></p></body></html>"))
        self.yesbill.setText(_translate("Dialog", "Billed"))
        self.nobill.setText(_translate("Dialog", "Not Billed"))
        self.backbutt.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Back to menu </span></p></body></html>"))
        self.backbutt.setText(_translate("Dialog", "Back To Reports"))

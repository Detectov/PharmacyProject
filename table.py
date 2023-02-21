import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication


class ProdWindow(QDialog):
    def __init__(self):
        super(ProdWindow, self).__init__()
        loadUi("prodtable.ui", self)

    def loaddata(self):
        med=[]

#main
app = QApplication(sys.argv)
prodwindow = ProdWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(prodwindow)
widget.setFixedWidth(1067)
widget.setFixedHeight(735)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Existing")



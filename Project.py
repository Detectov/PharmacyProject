from PyQt5.QtWidgets import *
from PyQt5 import uic
import os
os.system("cls")

class GUI(QMainWindow):
    
    
    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi("GUI.ui", self)
        self.show()
        
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(lambda: self.bingbong(self.textEdit.toPlainText()))
        self.actionClose.triggered.connect(exit)
    def login(self):
        if self.lineEdit.text() == "mou" and self.lineEdit_2.text() == "password":
            self.textEdit.setEnabled(True)
            self.pushButton_2.setEnabled(True)
        else:
            message = QMessageBox()
            message.setText("Invalid Login")
            message.exec_()
            
    def bingbong(self,msg):
        message = QMessageBox()
        message.setText(msg)
        message.exec_()
        

def main():
    app = QApplication([])
    window = GUI()
    app.exec_()
    
    
    
if __name__ == '__main__':
    main()
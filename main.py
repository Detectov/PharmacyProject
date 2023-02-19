import sys 
from  PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreated)
        
    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()
        print("Succesfully logged in with email: ",email, "and password",password)
        
    def gotocreated(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui",self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        
    def createaccfuntion(self):
        email = self.email.text()
        if self.paswword.text()==self.confirmpasss.text():
            password=self.password.text(
                print("Succesfully created acc with email " , email, "and password : ", password))
        
app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(620)
widget.setFixedHeight(480)
widget.show()
app.exec_()
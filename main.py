import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.loginbutton.clicked.connect(self.gotomenu)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreated)
        
    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()
        
        
        print("Succesfully logged in with email: ",email, "and password",password)
        
    def gotomenu(self):
        menu=Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
            
            
            
        
    def gotocreated(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui",self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        mail = []
        passes = []

        
    def createaccfunction(self):
        email = self.email.text()
        if self.password.text()==self.confirmpass.text():
            password=self.password.text()
            print("Succesfully created acc with email: " , email, "and password: ", password)
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)
            
class Menu(QDialog):
    def __init__(self):
        super(Menu, self).__init__()
        loadUi("menu.ui", self)
        widget.setFixedWidth(620)
        widget.setFixedHeight(480)
        self.addbutton.clicked.connect(self.gotoaddprod)
        self.reportbutton.clicked.connect(self.gotoreports)
        self.addsalebutton.clicked.connect(self.gotoaddsale)
        
    def gotoaddprod(self):
        addprod = AddProduct()
        widget.addWidget(addprod)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotoreports(self):
        reports = Reports()
        widget.addWidget(reports)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotoaddsale(self):
        addsale = AddSale()
        widget.addWidget(addsale)
        widget.setCurrentIndex(widget.currentIndex()+1)

class AddProduct(QDialog):
    def __init__(self):
        super(AddProduct, self).__init__()
        loadUi("addprod.ui", self)
        self.backbutton.clicked.connect(self.backtomenu)
        self.donebutton.clicked.connect(self.backtomenu)
        #done button creates the entered product as well
        
        
    def backtomenu(self):
        menu=Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class AddSale(QDialog):
    def __init__(self):
        super(AddSale, self).__init__()
        loadUi("createsale.ui", self)
        widget.setFixedHeight(480)
        widget.setFixedWidth(772)
        self.backbutton.clicked.connect(self.backtomenu)
        self.donebutton.clicked.connect(self.backtomenu)
        #done button creates the entered sale as well
        
    def backtomenu(self):
        menu=Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
     
        
class Reports(QDialog):
    def __init__(self):
        super(Reports, self).__init__()
        loadUi("report.ui", self)
        widget.setFixedWidth(620)
        widget.setFixedHeight(480)
        self.prodbutton.clicked.connect(self.gotoprodtab)
        self.salesbutton.clicked.connect(self.gotosalestab)
        self.backbutton.clicked.connect(self.backtomenu)
        
    def backtomenu(self):
        menu=Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotoprodtab(self):
        prodtable = ProdTable()
        widget.addWidget(prodtable)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotosalestab(self):
        salestable = SalesTable()
        widget.addWidget(salestable)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class ProdTable(QDialog):
    def __init__(self):
        super(ProdTable, self).__init__()
        loadUi("prodtable.ui", self)
        widget.setFixedWidth(1067)
        widget.setFixedHeight(735)
        self.backbutton.clicked.connect(self.backtoreports)
        
    def loaddata(self):
        pass
    
    def backtoreports(self):
        reports=Reports()
        widget.addWidget(reports)
        widget.setCurrentIndex(widget.currentIndex()+1)


class SalesTable(QDialog):
    def __init__(self):
        super(SalesTable, self).__init__()
        loadUi("saletable.ui", self)
        widget.setFixedWidth(1067)
        widget.setFixedHeight(735)
        self.backbutton.clicked.connect(self.backtoreports)
        
    def loaddata(self):
        pass
    
    def backtoreports(self):
        reports=Reports()
        widget.addWidget(reports)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(620)
widget.setFixedHeight(480)
widget.show()
app.exec_()
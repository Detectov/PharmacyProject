import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

import sys
from PyQt5 import QtWidgets, QtGui

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.username_label = QtWidgets.QLabel('Nombre de usuario')
        self.password_label = QtWidgets.QLabel('Contraseña')

        self.username_input = QtWidgets.QLineEdit()
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login_button = QtWidgets.QPushButton('Iniciar sesión')
        self.signup_button = QtWidgets.QPushButton('Registrarse')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.signup_button)
        self.setLayout(layout)

        self.login_button.clicked.connect(self.login)
        self.signup_button.clicked.connect(self.signup)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        with open('users.txt', 'r') as f:
            for line in f:
                u, p = line.strip().split(',')
                if u == username and p == password:
                    QtWidgets.QMessageBox.information(self, 'Inicio de sesión exitoso', '¡Bienvenido, {}!'.format(username))
                    widget.setCurrentIndex(widget.currentIndex()+1)
                    return

        QtWidgets.QMessageBox.warning(self, 'Inicio de sesión fallido', 'Nombre de usuario o contraseña incorrectos')

    def signup(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Debe ingresar un nombre de usuario y contraseña')
            return

        with open('users.txt', 'a') as f:
            f.write('{},{}\n'.format(username, password))

        QtWidgets.QMessageBox.information(self, 'Registro exitoso', '¡La cuenta de usuario ha sido creada!')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()  
    window.show()
    sys.exit(app.exec_())

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
        self.salesmenubutton.clicked.connect(self.gotosalesmenu)
        
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

    def gotosalesmenu(self):
        salesmenu = SalesMenu()
        widget.addWidget(salesmenu)
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

class SalesMenu(QDialog):
    def __init__(self):
        super(SalesMenu, self).__init__()
        loadUi("salesmenu.ui", self)
        widget.setFixedWidth(620)
        widget.setFixedHeight(480)
        self.cardbutton.clicked.connect(self.gotocards)
        self.cashbutton.clicked.connect(self.gotocash)
        self.backbutton.clicked.connect(self.backtoreports)

    def gotocards(self):
        cards = SalesByCard()
        widget.addWidget(cards)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocash(self):
        cash = SalesByCash()
        widget.addWidget(cash)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def backtoreports(self):
        reports=Reports()
        widget.addWidget(reports)
        widget.setCurrentIndex(widget.currentIndex()+1)

   


class SalesByCard(QDialog):
    def __init__(self):
        super(SalesByCard, self).__init__()
        loadUi("salesbycard.ui", self)
        widget.setFixedWidth(1067)
        widget.setFixedHeight(735)
        self.backbutton.clicked.connect(self.backtosalesmenu)

    def loaddata(self):
        pass
    
    def backtosalesmenu(self):
        salesmenu=SalesMenu()
        widget.addWidget(salesmenu)
        widget.setCurrentIndex(widget.currentIndex()+1)

class SalesByCash(QDialog):
    def __init__(self):
        super(SalesByCash, self).__init__()
        loadUi("salesbycash.ui",self)
        widget.setFixedWidth(1067)
        widget.setFixedHeight(735)
        self.backbutton.clicked.connect(self.backtosalesmenu)

    def loaddata(self):
        pass

    def backtosalesmenu(self):
        salesmenu = SalesMenu()
        widget.addWidget(salesmenu)
        widget.setCurrentIndex(widget.currentIndex()+1)

            
app=QApplication(sys.argv)
mainwindow=Login()

widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(620)
widget.setFixedHeight(480)
widget.show()
app.exec_()
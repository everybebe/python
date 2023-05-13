import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QMessageBox




form_class = uic.loadUiType("./pyqt09.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        self.pb0.clicked.connect(self.myclick)
        self.pb_call.clicked.connect(self.mycall)
    
    def mycall(self):
        str_tel=self.le.text()    
        QMessageBox.about(self,'calling',str_tel)
        
    def myclick(self):
        str_new= self.sender().text()
        str_old= self.le.text()
        
        self.le.setText(str_old+str_new)

        
    #     self.pb1.clicked.connect(self.myclick1)
    #     self.pb2.clicked.connect(self.myclick2)
    #     self.pb3.clicked.connect(self.myclick3)
    #     self.pb4.clicked.connect(self.myclick4)
    #     self.pb5.clicked.connect(self.myclick5)
    #     self.pb6.clicked.connect(self.myclick6)
    #     self.pb7.clicked.connect(self.myclick7)
    #     self.pb8.clicked.connect(self.myclick8)
    #     self.pb9.clicked.connect(self.myclick9)
    #     self.pb0.clicked.connect(self.myclick0)
    #     self.pb_call.clicked.connect(self.myclick)
    #
    # def myclick1(self):      
    #     self.number("1")
    # def myclick2(self):      
    #     self.number("2")
    # def myclick3(self):      
    #     self.number("3")
    # def myclick4(self):      
    #     self.number("4")
    # def myclick5(self):      
    #     self.number("5")
    # def myclick6(self):      
    #     self.number("6")
    # def myclick7(self):      
    #     self.number("7")
    # def myclick8(self):      
    #     self.number("8")
    # def myclick9(self):      
    #     self.number("9")
    # def myclick0(self):      
    #     self.number("0")
    # def myclick(self):  
    #     result = self.le.text()
    #     QMessageBox.about(self,'message',result)
    #
    #
    # def number(self,num):
    #     result = self.le.text()
    #     self.le.setText(result+num)
    #


        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()        
    
    
    
        

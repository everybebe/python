import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QMessageBox, QLabel
from _ast import For
import random


form_class = uic.loadUiType("./pyqt04.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
    
        

    
    def myclick(self):
        a = self.le1.text()
        b = self.le2.text()
        
        aa = int(a)
        bb = int(b)
        
        sum=0
        for i in range(aa,bb+1):
            sum += i
            
            
        self.le3.setText(str(sum))
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()        
    
    
    
        

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from _ast import If





form_class = uic.loadUiType("./pyqt07.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        #self.pb.returnPressed.connect(self.myclick) 엔터 누르면 바로 실행
        

    
    def myclick(self):
        a = int(self.le1.text());
        b = int(self.le2.text());
        c = int(self.le3.text());
        
        
        
        
        sum=0
       
        for i in range(a,b+1):
            if(i % c == 0):
                sum+=i
         
        self.le4.setText(str(sum))
                    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()        
    
    
    
        

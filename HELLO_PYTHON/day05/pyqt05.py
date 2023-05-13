import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random





form_class = uic.loadUiType("./pyqt05.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
    
        

    
    def myclick(self):
        

        mylist = list(range(1,45+1))
        
        for i in range(100):
            rnd = int(random()*45)            
            a = mylist[rnd]
            b = mylist[0]
            mylist[rnd] = b
            mylist[0] = a
        
        
        self.te1.setText(str(mylist[0]))  
        self.te2.setText(str(mylist[1]))   
        self.te3.setText(str(mylist[2]))  
        self.te4.setText(str(mylist[3]))   
        self.te5.setText(str(mylist[4]))   
        self.te6.setText(str(mylist[5]))   
        
        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()        
    
    
    
        

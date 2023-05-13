import sys
from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QIcon, QPushButton, QSize
from anaconda_navigator.utils.qthelpers import qapplication
from PyQt5.QtGui import QIconDragEvent, QIconEngine
from PyQt5.uic.Compiler.qtproxies import QtGui
from _ast import If

form_class = uic.loadUiType("./my_omok01.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.black= True
        self.pb.clicked.connect(self.myclick)
        
        
        for i in range(0,401,40):
            for j in range(0,401,40):
                temp = QPushButton('',self)
                temp.setIcon(QIcon('0.png'))
                temp.setIconSize(QSize(40,40))
                temp.setGeometry(i,j,40,40)
                temp.clicked.connect(self.myclick)
        
        # btn2 = QPushButton('',self)
        # btn2.setIcon(QIcon('0.png'))
        # btn2.setIconSize(QSize(40,40))
        # btn2.setGeometry(40,0,40,40)
        # btn2.clicked.connect(self.myclick)
        
        
    def myclick(self):
        if (self.black):
            self.sender().setIcon(QIcon('1.png'))
             
        else:
            self.sender().setIcon(QIcon('2.png'))
        self.black=not self.black    
           
if __name__ == "__main__":
    app = qapplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()        
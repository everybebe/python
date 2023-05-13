 import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from _ast import If





form_class = uic.loadUiType("./pyqt08.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        #self.pb.returnPressed.connect(self.myclick) 엔터 누르면 바로 실행
        

    
    def myclick(self):
        dan = int(self.le.text())

        txt = ""
        
        for i in range(1,9+1):
            txt += "{}*{}={}\n".format(dan,i,i*dan)
                    
        self.pte.setPlainText(txt)            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()        
    
    
    
        

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow





form_class = uic.loadUiType("./pyqt10.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb.clicked.connect(self.myclick)
    
  
    def getStar(self,cnt):
        ret=""
        for i in range(cnt):
            ret += "*"
            
        ret += "\n"
        return ret
    
    
    def myclick(self):
        
        aa = int(self.le_first.text())
        bb = int(self.le_last.text())
        
        txt = ""
        
        for i in range(aa,bb+1):
            txt += self.getStar(i)
     
        
        self.te.setText(txt)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()        
    
    
    
        

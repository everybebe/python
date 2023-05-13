import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QMessageBox, QLabel


form_class = uic.loadUiType("./pyqt02.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
    
        

    
    def myclick(self):
        
        a = self.lbl.text()
        aa = int(a)
        aa -= 1 
        self.lbl.setText(str(aa))
        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()        
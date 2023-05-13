import sys
from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QIcon, QPushButton, QSize, QMessageBox
from anaconda_navigator.utils.qthelpers import qapplication
from PyQt5.QtGui import QIconDragEvent, QIconEngine
from PyQt5.uic.Compiler.qtproxies import QtGui
from _ast import If
from conda.common._logic import TRUE

form_class = uic.loadUiType("./my_omok02.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        
        self.flag_dol = True
        self.flag_over = False
        
        self.arr2D=[
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0]
        
        ]
        self.pbs=[]
        
        self.setupUi(self)
        self.pb.clicked.connect(self.myreset)
        
        for i in range(10):
            for j in range(10):
                temp = QPushButton('',self)
                temp.setToolTip("{},{}".format(i,j))
                temp.setIcon(QIcon('0.png'))
                temp.setIconSize(QSize(40,40))
                temp.setGeometry(j*40,i*40,40,40)
                temp.clicked.connect(self.myclick)
                self.pbs.append(temp)   

        self.myrender()
    
    def myreset(self):
        print("myreset")
        
        self.arr2D=[
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0]
        
        ]
        
        self.myrender()
        
        self.flag_dol=True
        self.flag_over=False
        
    def myrender(self):

        for i in range(10):
            for j in range(10):
                if self.arr2D[i][j] == 0 :
                    self.pbs[i*10+j].setIcon(QIcon("0.png"))
                if self.arr2D[i][j] == 1 :
                    self.pbs[i*10+j].setIcon(QIcon("1.png"))
                if self.arr2D[i][j] == 2 :
                    self.pbs[i*10+j].setIcon(QIcon("2.png"))
    
    
    def myclick(self):

        if self.flag_over:
            return 
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2D[i][j] > 0 :
            return
        
        stone = -1
        
        if self.flag_dol:
            self.arr2D[i][j] = 1
            stone = 1
            
        else:
            self.arr2D[i][j] = 2    
            stone = 2
            
            
        up = self.UP(i,j,stone)
        dw = self.DW(i,j,stone)
        dl = self.DL(i,j,stone)
        dr = self.DR(i,j,stone)
        ri = self.RI(i,j,stone)
        li = self.LI(i,j,stone)
        ul = self.UL(i,j,stone)
        ur = self.UR(i,j,stone)
        
        
        d1 = up + dw 
        d2 = ul + ur 
        d3 = li + ri 
        d4 = ur + dl 
        

 
            
        self.myrender()
          
      
        if d1 == 4 or d2 ==4 or d3 ==4 or d4 ==4:
            if self.flag_dol:
                QMessageBox.about(self,'오목','흑돌승리')
            else:
                QMessageBox.about(self,'오목','백돌승리') 
            self.flag_over = True
        
        print(up,dw,dl,dr,  ri,li,ul,ur)    
                    
        self.flag_dol = not self.flag_dol
        
    
    def UP(self,i,j,stone):        
        
        cnt=0
        
        try:
            while True:
                i -= 1
                if i < 0:
                    return cnt
                if self.arr2D[i][j] == stone: 
                    cnt += 1
                else:
                    return cnt
        except:    
            return cnt    
        
    
    def DW(self,i,j,stone):        
        
        cnt=0
        
        try:
            while True:
                i += 1
                if i < 0:
                    return cnt
                if self.arr2D[i][j] == stone: 
                    cnt += 1
                else:
                    return cnt
        except:       
            return cnt
        
    
         

    def RI(self,i,j,stone):        
        
        cnt=0
        
        try:
            while True:
                j += 1

                if i < 0:
                    return cnt
                if self.arr2D[i][j] == stone: 
                    cnt += 1
                else:
                    return cnt
        except:       
            return cnt        
 
    def LI(self,i,j,stone):        
        
        cnt=0
        
        try:
            while True:
               
                j -= 1
                
                if i < 0:
                    return cnt
                if self.arr2D[i][j] == stone: 
                    cnt += 1
                else:
                    return cnt
        except:       
            return cnt     
        
        
    def UL(self,i,j,stone):        
        
        cnt=0
        
        try:
            while True:
                i -= 1
                j -= 1
                
                if i < 0:
                    return cnt
                if self.arr2D[i][j] == stone: 
                    cnt += 1
                else:
                    return cnt
        except:       
            return cnt         
        
        
    def UR(self,i,j,stone):        
        
        cnt=0
        
        try:
            while True:
                i -= 1
                j += 1
                
                if i < 0:
                    return cnt
                if self.arr2D[i][j] == stone: 
                    cnt += 1
                else:
                    return cnt
        except:       
            return cnt             
     
    def DR(self,i,j,stone):        
        
        cnt=0
        
        try:
            while True:
                i += 1
                j += 1
                
                if i < 0:
                    return cnt
                if self.arr2D[i][j] == stone: 
                    cnt += 1
                else:
                    return cnt
        except:       
            return cnt      
        
        
        
    def DL(self,i,j,stone):        
        
        cnt=0
        
        try:
            while True:
                i += 1
                j -= 1
                
                if i < 0:                                                                              
                    return cnt
                if self.arr2D[i][j] == stone: 
                    cnt += 1
                else:
                    return cnt
        except:       
            return cnt    
                       
    
        
if __name__ == "__main__":
    app = qapplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()        
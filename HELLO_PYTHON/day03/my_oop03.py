from day03.my_oop01 import Animal

class Human(Animal):
    
    def __init__(self):
        super().__init__()
        self.tools=[]
        self.tools.append("반지")
        
    def farming(self,tool):
        self.tools.append(tool)
        
    def __str__(self):       
        ret =str(self.tools)
        return ret

hum = Human()
print(hum.age)
print(hum)
hum.birthHappy()
hum.farming("돌도끼")
print(hum.age)
print(hum)
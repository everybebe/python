from boto.gs.lifecycle import AGE
        
class Animal:
        
    def __init__(self):
        self.age=1
        
    def birthHappy(self):   
        self.age += 1


if __name__ == '__main__':
    ani = Animal()
    print("11",ani.age)
    ani.birthHappy()
    print("12",ani.age)




# class animal:
#
#     def setdata(self):
#         self.age = 1
#
#         # a=animal()
#         # a.setdata(4,2)
#         # print(a.add())
#
#     def add(self, num):
#         self.result = num
#         return self.result
#
# age1 = animal()
#
# print(age1.add(3))

def showdan(dan):
    print("{} *{}={}".format(dan,1,dan*1))
    print("{} *{}={}".format(dan,2,dan*2))
    print("{} *{}={}".format(dan,3,dan*3))
    print("{} *{}={}".format(dan,4,dan*4))
    print("{} *{}={}".format(dan,5,dan*5))
    # print("{} *{}={}".format(dan,6,dan*6))
    print("{} *{}={}".format(dan,7,dan*7))
    print("{} *{}={}".format(dan,8,dan*8))
    print("{} *{}={}".format(dan,9,dan*9))



showdan(9)
showdan(7)
showdan(3)
showdan(2)

for i in range(2,9+1):
    if(i % 2==0):
        for j in range(1,9+1):
        
            result = str(i) + "*" + str(j) + "=" + str(i*j)
            print(result)  
    print("")
       
print("-----------------------------------------")


for i in range(2,9+1):
    if(i % 2==0):
        for j in range(1,9+1):
        
            result = str(i) + "*" + str(j) + "=" + str(i*j)
            print(result)  
    print("")
              
# for i in range(2,9+1):
#     for j in range(1,9+1):
#         result2 = "{}*{}={}".format(i,j,i*j)
#         print(result2)
#
#
#

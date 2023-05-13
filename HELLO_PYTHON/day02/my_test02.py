#첫 수를 입력하시오 5
#끝 수를 입력하시오 7
#5에서 7까지 합은 18입니다.

num1 = int(input("첫 수를 입력하시오"))
num2 = int(input("끝 수를 입력하시오"))

hap = range(num1,num2+1)

sum = 0
for i in hap: 
    sum += i

print("{}에서 {}의 합은 {}입니다.".format(num1,num2,sum))





#
# num3 = input("첫 수를 입력하시오")
# num4 = input("끝 수를 입력하시오")
# aa = int(num3)
# bb = int(num4)
#
# mylist = list(range(aa,bb+1))
#
#
# sum2 = 0
# for i in mylist:
#     sum2 += i
#
#
# print(num3 +"에서 " + num4 +"까지 합은" + str(sum2)+"입니다.")
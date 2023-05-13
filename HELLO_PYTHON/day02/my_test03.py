# 출력할 단수를 입력하시오 4
# 4 * 1 = 4
# 4 * 2 = 8


# 4 * 9 = 36


dan=input("출력할 단수를 입력하시오")
idan = int(dan)

num = range(1,9+1)

for i in num:
    result = idan*i
       
    print("{} * {} = {}".format(dan,i,result))
# 가위 바위 보를 선택하세요
# 나: 가위
# 컴: 바위
# 결과: 패배
from random import random

mine = ""
com =""
result =""

mine = input("가위 바위 보를 선택하세요")
rnd = random()

if rnd > 0.66:
    com ="가위"

elif rnd > 0.33:
    com = "바위"

else:
    com = "보"

if mine == com :
    result="무승부"    
elif mine == "가위" and com == "바위" or mine =="바위" and com == "보" or mine =="보" and com =="가위" :
    result="패배"
else:
    result="승리"
    

print("나", mine)
print("컴", com)
print("결과", result)

   
        
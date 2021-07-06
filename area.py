# area.py
# 반지름을 입력받아서 면적을 계산하는 프로그램

r = float(input("반지름 :"))
import math 
# pie = 3.14
area = r ** 2 * math.pi
print("원의 면적는", area , "입니다")


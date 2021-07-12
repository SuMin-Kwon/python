#t = 10, 20, 30
#print(t[0])


# 난수 3개를 생성해서 리턴 해주는 함수르 만듬
import random
def rnd3():
     a= random.randrange(1,10)
     b= random.randrange(1,10)
     c= random.randrange(1,10)
     return a, b, c   # 튜블로 값을 리턴해줌

print(rnd3())


# 매개변수의 난수를 받아서 함수를 만듬.
def rnd(n):
    cnt = []
    for i in range(n):
        s = random.randrange(1,10)
        cnt.append(s)
    return cnt

print(rnd(5))
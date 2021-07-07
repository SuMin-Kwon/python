# 숫자맟추기 게임 _ 야구


# 난수 3개 만들기
import random
c1 = random.randrange(1,10)
c2 = random.randrange(1,10)
c3 = random.randrange(1,10)
print(c1,c2,c3)

# c = 0
# while c < 10 :
#     u1, u2, u3 = map(int, input("숫자 3개를 입력하시요:").split(","))
#     s = 0
#     b = 0
#     c = c + 1
#     if c1 == u1 :   # 같은 값이면 스트라이크 증가
#         s += 1      # 
#     elif c1 == u3 or c1 == u2 :
#         b += 1

#     if c2 == u2 :
#         s += 1
#     elif c2 == u3 or c2 == u1  :
#         b += 1

#     if c3 == u3 :
#         s += 1
#     elif c3 == u2 or c3 == u1 :
#         b += 1
#     if s == 3 :
#         print("성공!!!")
#         break
#     else :
#         print("스트라이크는 {}이고, 볼은 {}입니다.".format(s,b))    
        
# print("끝")

s = 0
b = 0
c = 0
while s < 3 :
    u1, u2, u3 = map(int, input("숫자 3개를 입력하시요:").split(","))
    s = 0    # 초기화 값
    b = 0    # 초기화 값
    c = c + 1
    if c1 == u1 :   # 같은 값이면 스트라이크 증가
        s += 1      # 
    elif c1 == u3 or c1 == u2 :
        b += 1

    if c2 == u2 :
        s += 1
    elif c2 == u3 or c2 == u1  :
        b += 1

    if c3 == u3 :
        s += 1
    elif c3 == u2 or c3 == u1 :
        b += 1
    if c > 10 :
        print("게임종료!!!")
        break
    else :
        print("스트라이크는 {}이고, 볼은 {}입니다.".format(s,b))    
        
print("정답!!!!!")
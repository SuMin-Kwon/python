# 삼각형 출력
# range(e)   0 ~ e-1 
# ragne(s, e)    s ~ e-1
# range(s, e, step)   s ~ e-1 , step 수만큼 차이남

# 다이아몬드 만들기
# cnt = 10
# for i in range(0,cnt) :
#     print(" " * (cnt-i) , end='' )
#     print("*" * (i*2+1))

# for i in range(0,cnt-1) :
#     print(" " * (i+2), end ="")
#     print("*" * (((cnt-i-1)*2-1)))

# 트리높이 구하기
line = int(input("트리의 높이를 입력하세요(1~30)"))
# for i in range(0,tree) :
#      print(" " * (tree-i) , end='' )
#      print("*" * (i*2+1))
# for i in range(0,3):
#     print(" " * (tree - 1), end='')
#     print("*" * 3 )
    
for x in range(1,line+1):
    print(" "* (line-x) + ("*" * (x*2 -1)))
for y in range(1,4):
    print(" "* (line-2) + "***")
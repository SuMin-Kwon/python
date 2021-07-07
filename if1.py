# 입력받은 두수가 모두 10보다 큰지 검사
n1, n2 =map(int, input("두 수 입력 >").split())

# 조건이 참이 아닌 경우에는 안에 들어간 내용은 실행되지 않음
if n1>10 and n2>10 :
    print("모두 10보다 크다")

else :
    print("10보다 크지 않다")

print("The End")
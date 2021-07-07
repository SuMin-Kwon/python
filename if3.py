# 숫자를 홀수,짝수로 구분

number = input("정수를 입력 :")

l = int(number[-1])

if l == 0 or \
    l == 2 or \
    l == 4 or \
    l == 6 or \
    l == 8 :
    print("짝수입니다.")

if l == 1 or \
    l == 3 or \
    l == 5 or \
    l == 7 or \
    l == 9 :
    print("홀수입니다.")
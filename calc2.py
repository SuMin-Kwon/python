# 두 수를 연산자를 입력 받아서 사칙연산하는 프로그램

num1, num2 = map(int, input("두수를 입력").split())
op = input("연산자:")

if op == "+" :
    print("두 수의 합은",num1 + num2,"입니다.")
elif op == "-" :
    print("두 수의 뺄셈은",num1 - num2,"입니다.")
elif op == "*" :
    print("두 수의 곱셈은",num1 * num2,"입니다.")
elif op == "/" :
    print("두 수의 나눗셈은",num1 // num2,"입니다.")
elif op == "%" :
    print("두 수의 나머지는",num1 % num2,"입니다.")

# calc.py 백준 10869번
# 두 수를 입력받아서 사칙연사하는 프로그램

num1, num2 = map(int, input("두수를 입력").split())
a = num1 + num2
b = num1 - num2
c = num1 * num2
d = num1 // num2
e = num1 % num2

print("두 수의 합은",a,"입니다.")
print("두 수의 뺄셈은",b,"입니다.")
print("두 수의 곱셈은",c,"입니다.")
print("두 수의 나눗셈은",d,"입니다.")
print("두 수의 나머지는",e,"입니다.")
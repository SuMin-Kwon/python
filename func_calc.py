# num1, num2 = map(int, input("두수를 입력").split())
# op = input("연산자:")

def func_calc(a, b, c) :
    result = 0
    if c == "+" :
        result = a + b
    elif c == "-" :
        result = a - b
    elif c == "*" :
        result = a * b
    elif c == "/" :
        result = a // b
    elif c == "%" :
        result = a % b
    return result
    
r = func_calc(10, 20, "*")
print(r)
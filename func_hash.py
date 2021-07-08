
def func_tri(n):
    # for i in range(n):
    #     print(" " * (n-i) + "*" * ((i*2)+1))   삼각형일때
    for i in range(1, n+1):
        print("*" * i)              # 반쪽 삼각형일때


func_tri(5)
print()
func_tri(3)
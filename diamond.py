
cnt = 10
for i in range(0, cnt+1):
    print(" " * (cnt-i), end="")
    print("*" * (i*2+1))
for i in range(cnt, 0, -1):
    print(" " * (cnt-i+1),end="")
    print("*" * (i*2-1)) 
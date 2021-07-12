def gugu(n):
    r = 0
    for e in range(1,10):
        r = n * e
        print(n, "*", e, "=",r)

n = int(input("구구단 수 :"))
gugu(2)
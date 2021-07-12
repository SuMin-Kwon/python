a = int(input("숫자:"))
for e in range(1,a+1):
    print(" "* (a-e) + "*" * ((2 * e)-1))
for e in range(a,0,-1):
    print(" "* (a-e+1) + "*" * ((2 * (e-1))-1))
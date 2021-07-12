def min_int(a,b,c):
    if a > b :
        t = a
        a = b
        b = t
    if b > c :
        t = b
        b = c
        c = t
    if a > b:
        t = a
        a = b
        b = t
    return a,b,t


a,b,c =map(int,input("세 개 :").split())
print(min_int(a,b,c))

def star(n):
    for e in range(1,n+1):
        print("*"* e)
    for e in range(n,0,-1):
        print("*"* (e-1))    

star(3)
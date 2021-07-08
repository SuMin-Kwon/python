

def f_2577(a, b, c):
    cnt = [0,0,0,0,0,0,0,0,0,0]
    abc =str( a * b * c )
    for i in abc : 
        cnt[int(i)] += 1
    return cnt

li = f_2577(150,266,427)
for i in li :
    print(i)
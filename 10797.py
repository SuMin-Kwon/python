

def func10(day,car):
    cnt = 0
    for e in car :
        if e == day :
            cnt += 1   
    return cnt
 
day = int(input("날짜"))
car = list(map(int,input("차량번호").split()))
print(func10(day,car))

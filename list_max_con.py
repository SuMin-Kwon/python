# 리스트 안에 최대값을 구하는 방법

li = [20, 30 ,40, 50, 100]
m = 20
mm = 20
# 리스트 수만큼 반복
for i in li :
    if i < m :
        continue   # 조건식에 맞지 않을 경우에는 다시 위로 돌아감
    m = i    
print("최대값:{}".format(m))



# 리스트 안에 최대값을 구하는 방법

li = [20, 30 ,40, 50, 100]
m = 20
mm = 20
# 리스트 수만큼 반복
for i in li :
    if i < m :
        m = i 
    if i > m :
        mm = i    
print("최솟값:{}, 최댓값은:{}".format(m,mm))



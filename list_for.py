# 리스트안에 for 문 사용
# 조건에 맞는 갯수를 알고자함

cnt = 0
li = [10,20,35,15]
for i in li :
    if i <= 20 :
        continue # 20보다 작은수면 다시 돌아감 
    print(i)
    cnt += 1
        
print("맞는 갯수 :",cnt)        
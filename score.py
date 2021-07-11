
# 3반의 영어 성적
eng = [
    [90,70,30],
    [100,50],
    [60,50,50,70]
]

sum_eng = 0
for i in range(len(eng)) :
    for j in range(len(eng[i])) :
        sum_eng += eng[i][j]
print(sum_eng)
print("--------------------")
sum_eng2 = 0
for e in eng :
    for e1 in e :
        sum_eng2 += e1
print(sum_eng2)
print("--------------------")

ban_sum = 0

#for b in range(len(eng)) :
#    print(b+1,"반:",sum(eng[b]))
for b in range(len(eng)) :
    ban_sum += eng[b][1]
    print(ban_sum)
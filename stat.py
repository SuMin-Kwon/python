# 10 ~ 30대까지 몇명인지 파악한 후 명 수 만큼 #으로 표현하기

# 1 ~ 9 : ?
# 10 ~ 19 : ? ##
# 20 ~ 29 : ? ##
li = [15, 11, 24, 39 , 23]
cnt = [0,0,0,0]

for i in li : 
    r = i // 10
    cnt[r] += 1
for e in cnt :
    print("#" * e )


# for i in cnt :
#     print()

# 라운드 4 / 
# 5 6
# 6 6
# 4 3
# 5 2


chang = 100
sang = 100

c = int(input("라운드 입력 :"))

for i in range(c) :   # 0,1,2,3 / 0 ,1, 2, 3
    ch_dice ,s_dice = map(int,input("창영,상덕 주사위 값? :").split(","))  
    if ch_dice < s_dice :
        chang = chang - s_dice

    elif ch_dice > s_dice :
        sang = sang - ch_dice

print("창영이 점수 :",chang,"상덕이 점수 :",sang)


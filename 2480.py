# 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다. 

# 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다. 
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다. 
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.  

dice1,dice2,dice3 = map(int,input("주사위 결과 입력 :").split(","))
li = [dice1, dice2, dice3]
print(li)
if dice1 == dice2 == dice3 : # 같은 눈 3
    sum1 = 10000 + ( dice1 * 1000 )
    print("상금은 {:,}원입니다.".format(sum1))
elif dice1 == dice2 :   # 같은 눈 2
    sum1 = 1000 + (dice1 * 100)
    print("상금은 {:,}원입니다.".format(sum1))
elif dice2 == dice3 :   # 같은 눈 2
    sum1 = 1000 + (dice2 * 100)
    print("상금은 {:,}원입니다.".format(sum1))
elif dice1 == dice3 :   # 같은 눈 2
    sum1 = 1000 + (dice1 * 100)
    print("상금은 {:,}원입니다.".format(sum1))
else :
    sum1 = 100 + max(li) * 10 # 같은 눈이 없을때 최대값
    print("상금은 {:,}원입니다.".format(sum1))
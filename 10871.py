# 백준 10871문제

n,x = map(int, input("두 수 입력:").split())
li = list(input().split())
cnt = 0
# 리스트 반복
for i in li :
# x 보다 작으면 카운트 증가
    if int(i) < x :
        print(i, end=" ")
        cnt += 1
# 카운트 출력
print("건수", cnt)
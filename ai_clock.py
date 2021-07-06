# ai_clock 인공시계 문제
# 1. 시 분 초 입력
# 2. 요리시간 입력
# 3. 요리시간을 60초로 나누어서 나머지를 구함
# 4. 현재시간 초에 더하고 60이상이면 60으로 나눈 몫은 올림수로 올리고 나머지는
#    초로 둔다. 
#    분에 올림수를 더하고 60이상으로 넘어가면 나눈 몫은 올림수로 올리고 나머지는
#    분으로 둔다.
#    분의 올림수를 시에 더하고 시가 23 이상이면 다시 -23을 뺴주면 되지 않을까?.... 
# 5. 요리시간을 60초로 나누어서 몫을 구하면 분이 계산됨.
# 올림수와 요리시간 분을 현재시간에 더하고 60이상이면....

# 시는 % 24 나눔

#si, boon, cho = map(int, input("시간을 입력세요(,)").split(","))
#cook = int(input("요리시간 > "))
#boon += cook % 60
# si가 60보다 큰지 검사
#cho += cook // 60
# boon가 60보다 큰지 검사
# si에 boon을 올림수

# 내가 코드 짠거
#boon_a = boon + (cook // 60)
# cho_a = cho + (cook % 60)
#print("맛있는 요리의 시간은",si,"시",boon,"분",cho,"초 입니다.")

h ,m, s = map(int,input().split())
time = int(input())

# 초 계산
s = s +time
up = s // 60
s = s % 60

# 분 계산
m = m +time
up = m // 60
m = m % 60

# 시 계산
h = h + up
h = h % 24

print(h, m , s)

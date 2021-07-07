"""
1.설문조사를 한 사람의 수  : 5 
2. 인원수만큼 반복해서 값을 입력받아서 리스트에 추가합니다.  : for , append
3. 리스트의 요소 수대로 반복해서  for
    큐트이면 카운트증가    if
4. 설문조사 수에서 카운트 증가수보다 크면 큐트고 아니면 안 큐트  : if
"""
#조사인원
su = int(input("설문조사인원:"))
c = 0
answer = []

for i in range(su) :
    answer.append(input("귀여우면 0, 아니면 1 입력 :"))

# 처리
for t in answer :
    if t == "1" :
        c += 1

# 출력
print(answer)
if c > su-c :
    print("cute")
elif c == su-c :
    print("normal") 
else :
    print("not cute")

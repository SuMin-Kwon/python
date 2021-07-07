# 점수를 입력 받아서 등급 계산
# >90 수 >80 우 나머지는 기타 
# 
score = int(input("점수 입력하세요:"))

# 등급계산(처리)
if score > 90 :
    grade = "수"
elif score > 80 :
    grade = "우"
else :
    grade = "기타"

# 결과 출력
print("결과: ", grade)
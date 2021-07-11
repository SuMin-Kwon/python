# 학생 4명의 국어,영어,수학 성적을 저장
score = [
    [50,70,30],
    [100,50,40],
    [50,85,70],
    [80,60,70]
]

eng_total = 0

for std in score:
    eng_total += std[1]     # range 범위 없이 구하는 방법

print(eng_total)

for i in range(len(score)):    # range 범위로 구하는 방법 / 인덱스를 정해서 더해줌
    eng_total += score[i][1]

print(eng_total)
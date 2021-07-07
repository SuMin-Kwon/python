# 리스트에 요소를 추가/삭제/삽입/조희

f_list = ["이나은","백명진","진아름"]

# 추가 append() / extend는 여러가지 요소를 추가할 수 있다
f_list.append("권수민")
print(f_list)

# 삽입 insert(i ,v) / i 는 위치 / v는 추가요소
f_list.insert(2, "강성중")
print(f_list)

# 조회 [index]
print(f_list[1])

# 수정
f_list[1] = "홍길동" 
print(f_list)

# 삭제
f_list.pop()  # 아무것도 안치면 맨 마지막꺼 지움
f_list.pop(0)
del f_list[1]
print(f_list)

f_list.remove("홍길동")
print(f_list)

#검색 in
f_list = ["이나은","백명진","진아름"]
print("이나은" in f_list)

# 모두제거
# f_list.clear()
# print(f_list)
print()
# 전체조회
for n in f_list : # f_list안에 있는 갯수만큼 for문을 반복할꺼임
    print("{} {}".format(n[0],n[1:])) # 성 다음 이름 두개가 나오도록 할때

print("조회완료")
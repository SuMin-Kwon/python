# 이름을 입력받아서 리스트에서 검색한 결과를 출력
# 검색 : 김유신
# 있으면 있다 없으면 없다고 출력
# strip()은 값의 양쪽 공백을 빼주고 값의 중간의 들어간 공백은 없앨 수 없슴

f = ["김유신", "이순신", "유관순" ]
name = input("이름을 입력하세요>").strip()

if name in f :
    print("있다")
else :
    print("없다")
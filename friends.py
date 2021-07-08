# 친구 추가,삭제,검색 하는 프로그램
# append del in 

fr = ["홍길동","권수민"]
no = "1"    # while의 빠져나갈 조건을 적기 위해서는 no의 값을 줘야함
            # no값에 아무것도 없으면 while의 조건이 아예 성립하지 않아서 에러가 남
while no != "0" :
    no = input("0.종료 1. 추가 2.삭제 3.검색 4.전체조회:")
    if no == "1" :
        name = input("추가할 이름:")
        fr.append(name)
    elif no == "2" :
        name = input("삭제할 이름:")
        fr.remove(name)
    elif no == "3":
        name = input("검색할 이름:")
        print(name in fr )
    elif no == "4" :
        for e in fr :
            print(e)
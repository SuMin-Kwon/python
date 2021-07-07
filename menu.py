# 메뉴 번호 입력받아서 해당메뉴를 출력 반복 실행
# 메뉴번호를 0을 입력하면 종료

prices = [4000,5000,7000,6000,5500]
menu_list = ["아메리카노","카페라떼","아포카토","딸기스무디","카페모카"]

list2 = len(menu_list)
c = 0
while c < 5 :
    no = int(input("메뉴번호입력(1~{})".format(list2)))
    if no == 0 :
        break
    print("{}가격은{:,}원 입니다.".format(menu_list[no-1],prices[no-1]))
    c += 1


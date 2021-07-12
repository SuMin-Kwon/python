dic = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ing" : [ "망고", "설탕", "황산나트륨", "황색소"],
    "origin" : "필리핀"
}

dic["price"] = 5000
v = dic.get("존재하지 않는 키")
use = input("입력하세요 :")
while True :
    if "종료" == use :
        break

    elif use in dic:
        print(dic[use])
        use = input("입력하세요 :")

    elif v == None :
        print('잘못된 접근입니다.')         
        use = input("입력하세요 :")


# with open("basic2.txt","r") as file:  # 읽기모드
#     print(file.read())

with open("basic2.txt","r") as file:  # 읽기모드
    for line in file : # print(file.readline())       line = i랑 똑같음
        a,b = map(int, line.split())    # 자동으로 엔터가 들어감
        print(a+b)
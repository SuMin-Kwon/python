# file = open("basic.txt","w")
# file.write("파일 열어보기 예제, hello everyone!")
# file.close()   # 닫아줘야지만 꼭 파일이 저장됨


with open("basic2.txt","w") as file:
    file.write("파일 열어보기 예제, hello everyone!")


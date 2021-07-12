
def ota(a):
    
    for i in range(a):
        b,c= input("숫자,문자입력:").split()
        b = int(b)
        li =list(c)
        del li[b-1]
        print(b,"".join(li))

a = int(input("오타문자열 갯수:"))
ota(a)
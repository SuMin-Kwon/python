
# 함수 선언
def greet():
    for i in range(3):
        print("안녕")
    # return 생략되어있다고 보면 됨
    
def greet_3times(name,n) :
    print(name)
    for i in range(n):
        print("안녕하세요")
                                  # 실행 순서 8행 > 함수호출로 점프해서 3행 > 4행 > 5행 > 6행 > 다시 원래 위치로 돌아옴 (리턴)
greet_3times("홍길동",4)          # 함수 실행(함수 호출)
greet_3times("권수민",1)
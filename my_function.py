# 10 을 받으면 ====== 나오도록 만들어보세요

def print_line(a):
    print("=" * a )
    print("=" * a )


# 매개변수 : int형 2개
# 리턴 : 큰 수
def my_max(n,m):
    r = 0
    if n > m :
        r = n
    else :
        r = m
    return r

# 합계 계산
def my_sum(*a):
    r = 0
    for i in a :
        r += i
    return r
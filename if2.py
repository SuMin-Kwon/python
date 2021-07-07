# 입력받은 숫자가 홀수이면 홀수라고 출력

a = int(input("숫자를 입력하세요 :"))
a = a % 2 

if a == 1 :
    print("홀수입니다.")

else :
    print("짝수입니다.")

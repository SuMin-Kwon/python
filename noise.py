# eval 함수를 사용해서 풀 수 있슴


a = int(input('a :'))
c = input('*, + 중 하나를 입력 :')
b = int(input('b :'))
print(eval('{} {} {}'.format(a,c,b)))
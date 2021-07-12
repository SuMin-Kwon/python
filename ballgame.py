# 숫자야구게임
# 컴퓨터가 임의 숫자 3자리를 뽑도록한다.
# (여기서 임의 숫자는 겹치지 않도록 설정한다.)
# 임의 숫자를 변수에 저장한다.
# 유저가 숫자 3자리를 입력한다.
# 컴퓨터 임의 숫자 {a, b, c} / 유저 입력 숫자 {e, f, g}
# a == b and b == f and c == g  > 게임승리 
# a == b and c == g > 스트라이크 투
# a == e and b == f > 스트라이크 투
# b == f and c == g > 스트라이크 투
# a == e or b == f or c == g > 스트라이크 원
# if e in [b,c] and f in [a,c] and g in [a,b] : 쓰리볼
# if e in [b,c] and f in [a,c] : 투볼
# if f in [a,c] and g in [a,b] : 투볼
# if e in [b,c] and g in [a,b] : 투볼
# if e in [ b , c ] : 원볼
# if f in [ a , c ] : 원볼
# if g in [ a , b ] : 원볼 
# 원볼 or 스트라이크원 or 스트라이크 투 or 투볼 or 쓰리볼일떄
# 입력으로 돌아가서 숫자를 다시 입력하게함




import random
a = random.random(1,9)
b = random.random(1,9)
c = random.random(1,9)

if a == b or b == c or a == c :
   



cum = '{0} {0} {0} '.format(a,b,c)
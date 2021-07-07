# 숫자 맟추기 게임

""" 1. 임의의 수 생성
2. 숫자 입력
3. 입력값이 크다면 크다라고 출력
4. 입력값이 작으면 작다라고 출력
5. 입력값이 맞으면 맞다라고 출력 하고 프로그램 종료 exit()

6. 2~5번까지를 4번 복사해서 반복
7. "게임오버"라고 출력
 """

import random
com = random.randrange(1,10)

use = int(input("임의의 수를 입력하세요 :"))
if use > com :
    print("크다")
elif use < com :
    print("작다")
elif use == com :
    print("와우!")
    exit()

use = int(input("임의의 수를 입력하세요 :"))
if use > com :
    print("크다")
elif use < com :
    print("작다")
elif use == com :
    print("이열~")
    exit()

use = int(input("임의의 수를 입력하세요 :"))
if use > com :
    print("크다")
elif use < com :
    print("작다")
elif use == com :
    print("오....")
    exit()

use = int(input("임의의 수를 입력하세요 :"))
if use > com :
    print("크다")
elif use < com :
    print("작다")
elif use == com :
    print("아슬아슬했네..?")
    exit()

print("◇◇게임오버◇◇")

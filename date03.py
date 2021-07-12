import datetime
now = datetime.datetime.now()

if 3 <= now.month <= 5 :
    print("현재 계절은 \"봄\"입니다.")

if 6 <= now.month <= 8 :
    print('현재 계절은 \"여름\"입니다.')

if 9 <= now.month <= 11 :
    print('현재 계절은 \"가을\"입니다.')

if 12 == now.month or 1 <= now.month <= 2 :
    print('현재 계절은 \"겨울\"입니다.')    
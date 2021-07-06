# format() 함수 연습

money = 5000
print("{0:,}만원".format(money))   #   = print(money,"만원") , 콤마
print("{0:010,d}만원".format(money))  #  10자리로 출력
print("{0:+d}만원".format(money))  #  부호를 붙여서 출력해주세요
print("{0:08d}만원".format(money))  #  8자리로 출력 빈자리 0을 채움
print()
print()
print('{0:↘^50}'.format("메뉴판") )
print("                                                        ")
print('{0:>17} 메뉴는 {1:,}원입니다.'.format("김치찌개", money) )
print('{0:>17} 메뉴는 {1:,}원입니다.'.format("부대찌개", money) )
print(' %17s 메뉴는 %d 원입니다.'%("된장찌개", money) )
print()
print()
avg1 = 89.23
avg2 = 90.2
print('{:^24}'.format("성적") )
print("---------------------------")
print('평균1={:6.1f}, 평균2={:6.1f}'.format(avg1, avg2)) # 전체 6자리 소숫점은 한자리
print('평균1= %6.1f, 평균2= %6.1f' %(avg1, avg2) )

# 
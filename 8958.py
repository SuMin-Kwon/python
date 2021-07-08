# 라운드 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX

r = int(input("라운드 입력:"))  # 라운드 값 입력
ra = 0                          # 초기 테스트 결과 값
wa = 0                          # 초기 ra의 순서값

for i in range(r) :             # 라운드 회차 
    ox = input("정답:")         # o,x 입력받음
    ox_len = len(ox)            # 입력받은 o와 x의 갯수를 변수값에 저장

    ra = 0                      # 회차 초기화 값
    wa = 0                      # 회차 초기화 값
    for e in range(ox_len) :    # 입력받는 ox의 갯수만큼 돌려서 결과값을 구함

        if "O" == ox[e] :       # 입력받은 ox 중 o 일 경우
            ra = ra + ((e + 1) - wa)

        elif "X" == ox[e] :     # 입력받은 ox 중 x 일 경우
            wa = ( e + 1 ) * 1
         
    print(ra)        
    



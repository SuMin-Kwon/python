# string.py
id = "930126-2787910"

# 성별 출력
print("성별은", id[7])
# 출생년도 출력
print("출생년도는", id[:2])
# 몇월생
print("생년월은", id[2:4])
# 마지막 숫자 - 뒤에서 두번째 자리부터 끝까지 나오게 하려고 할떄
print("마지막 숫자는", id[-2:])
print(id[14]) # 범위를 넘어서면 Index Error 뜸
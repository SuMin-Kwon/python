# calc_test.py

#import calc as c   # calc 있는걸 다 불러오는데 c로 사용하겠다
from calc import Calc


# a = 4
# b = 5
c = Calc(14,15)

print(c.add())   # 위에서 calc 별칭을 c로 변경해서 이렇게 씀
print(c.sub())
print(c.mul())
print(c.div())
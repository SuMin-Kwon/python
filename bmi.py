# 비만도 계산 방법 (BMI지수)
# BMI지수 = 몸무게(kg) / ( 신장 * 신장 )
# 산출된 값이 18.5 이하면 저체중
# 18.5 ~ 23 정상
# 23 ~ 25 과체중
# 30이상은 고도비만으로 나누어진다.

kg = float(input('몸무게를 입력하세요(kg) >'))
cm = float(input('키를 입력하세요(cm) >'))
# '평균1= %6.1f, 평균2= %6.1f' %(avg1, avg2) )

g = ""
bmi = kg / (cm/100 * cm/100)
if bmi < 18.5 :
    g = "저체중"
elif bmi < 23 :   # 18.5 <= bmi < 23 이 조건은 파이썬만 사용 가능함, 다른곳에서는 X
    g = "정상"    # 위에서 이미 18.5 이상의 조건으로 걸러졌기 때문에 굳이 18.5 <= 는 안써도됨
elif bmi < 25 :
    g = "과체중"
else :
    g = "고도비만"

print("당신의 BMI 지수는 {:0.2f}이고 결과는 {}입니다.".format(bmi,g))
#    bmi 지수를 format 함수를 사용해서 {} 넣은다음 {}의 소숫점을 몇자리까지 표시하는지 표시하면 됨
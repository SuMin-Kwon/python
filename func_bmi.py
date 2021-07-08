

def result_sum(cm, kg):
    bmi = kg / (cm/100 * cm/100)
    if bmi < 18.5 :
        g = "저체중"
    elif bmi < 23 :   
        g = "정상"    
    elif bmi < 25 :
        g = "과체중"
    else :
        g = "고도비만"
    return g


result = result_sum(160, 60)
print(result)
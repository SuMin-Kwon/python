# key : value
# key로 값을 추가하거나 key로 값을 조회/삭제


        #사번 ,name , email
emp = [ ["100","홍길동","a@a.a"],
        ["101","권수민","a@b.a"],
        ["100","홍길동","a@a.a"],
]

# 두번재 사원의 이름을 출력
emp_name : 0
name = input("이름")
find_result = False
# for e in range(len(emp)) :
#     if name == emp[e][1] :
#         print("{}행에".format(e+1),"있다")
#         break
#     else :
#         print("{}행에".format(e+1),"없다")
for i in range(len(emp)):
    if name == emp[i][1]:
        find_result = True
        break
if find_result :
    print("있다")
else:
    print("없다")

#### list --> diction
emp1 = {"no":"100","name":"홍길동","mail":"a@a.a"}
print(emp1["name"])
emp_dic = [ {"no":"100","name":"홍길동","mail":"a@a.a"},
        {"no":"101","name":"권수민","mail":"a@b.2"},
        {"no":"102","name":"이나은","mail":"a@c.3"},
]
print("두번째 사원의 이름은:", emp_dic[1]["name"])
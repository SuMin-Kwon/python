a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))

cnt = [0,0,0,0,0,0,0,0,0,0]
abc =str( a * b * c )

for i in abc : 
    cnt[int(i)] += 1
for i in cnt :
    print(i)

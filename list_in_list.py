li = [[0,2,3],
      [4,1,6],
      [7,8,2]]

print("마지막요소:", li[1][1])

# for e in li:
#     print(e)

for i in range(len(li)):
    for j in range(len(li[i])):
        if i == j :
            print(li[i][j])    # i행과 j열이 같은 경우만 출력

list = [[1,2,3],[4,5,6],[7,8,9]]
for i in list:
    for j in i:
        if j == 3:
            continue
        print(j)
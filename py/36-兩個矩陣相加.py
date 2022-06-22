# 兩個矩陣相加

X = [[2,7,3],
    [4 ,5,6],
    [1 ,8,9]]

Y = [[4,8,1],
    [6,7,3],
    [2,5,9]]

r = [[0,0,0],
    [0,0,0],
    [0,0,0]]

for i in range(len(X)):                  # 列相加  
   for j in range(len(X[0])):            # 欄相加
       r[i][j] = X[i][j] + Y[i][j]

for r in r:
   print(r)

# 兩個矩陣相乘

# 3x3 矩陣
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

# 3x4 矩陣
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

# 結果為 3x4 矩陣
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
   

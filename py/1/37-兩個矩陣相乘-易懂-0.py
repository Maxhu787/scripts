# 設定 X 陣列
X = [[1,7,3],
    [4 ,5,6],
    [2 ,8,9]]
 
# 設定 Y 陣列
Y = [[5,8,1],
    [6,7,3],
    [4,2,9]]
 
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
 
print('印出 X')
for i in range(3):
    for j in range (3):
        print(X[i][j], end=' ')
    print()
print()
 
print('印出 Y')
for i in range(3):
    for j in range (3):
        print(Y[i][j], end=' ')
    print()
print()    
 
m1=0;m2=0;m3=0
for i in range(3):
    for j in range(3):
        print('x(',i,j,')','y{',j,'0)','X[',i,j,'], Y[',j,'1]','X[',i,j,']','Y[',j,'2]')
        m1=m1+X[i][j]*Y[j][0] ; m2=m2+X[i][j]*Y[j][1] ; m3=m3+X[i][j]*Y[j][2]
        
    result[i][0]=m1           ; result[i][1]=m2       ; result[i][2]=m3
    
    print('%3d %3d %3d' % (m1,m2,m3)) # 印出結果
    m1=0;m2=0;m3=0
    print()
 
for r in result:             # 印出陣列值
    print(r)

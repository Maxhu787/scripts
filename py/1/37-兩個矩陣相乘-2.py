# 兩個矩陣相乘


'''
https://goo.gl/pP2KbL

可到這裡驗證 
https://goo.gl/EyZ3Bf

本題矩陣相乘 結果圖形
https://i.imgur.com/Xae6kWn.jpg

X =
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)

X*Y=
x(0,0)*y(0,0)+x(0,1)*y(1,0)+x(0,2)*y(2,0)  ...  ...
...                                        ...   ...
...                                        ...   ...

'''


X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

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
# 列相乘

    # 欄相乘
for j in range(3):
    for k in range(3):
        m1=m1+X[j][k]*Y[k][0]
        m2=m2+X[j][k]*Y[k][1]
        m3=m3+X[j][k]*Y[k][2]        
    print('%3d %3d %3d' % (m1,m2,m3))
    m1=0;m2=0;m3=0
    print()    
        

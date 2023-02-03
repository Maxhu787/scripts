# 巴斯卡三角形 (二維串列)

p=[ [0] * 30 for i in range(20)] # 先產生 p 串列

n=10

p[0][1]=1

for i in range(1,(n+1)+1):
    for j in range(1,(n+1)+1):
        p[i][j]=p[i-1][j]+p[i-1][j-1]      # 計算數值
        
for i in range(0,n+1):
    print(2*(n-i)*' ',end='')              # 定位
    for j in range(1,(i+1)+1):
        print("%4d" %( p[i][j]), end='');  # 印出
    print()





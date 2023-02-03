# 二維陣列 : 產生 、 設定、呼叫

p=[ [''] * 5 for i in range(10)]

for i in range(10):
    for j in range(5):
        p[i][j]=str(i)+','+str(j)


for i in range (10):
    for j in range(5):
        print(p[i][j],end='   ')
    print()    

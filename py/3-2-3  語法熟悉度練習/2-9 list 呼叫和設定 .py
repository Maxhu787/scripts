# (練習: 2-9). 
a = [2,4,6,8,10]                     # 設定串列
for i in range(0, len(a)): 
    print(a[i]*a[i]) 
    a[i] = a[i]*a[i] 
    print(a) 

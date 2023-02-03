# 三位數 三次方阿姆斯壯數
for n in range(1,1000):
    s=0
    for i in range(3):
        # 1~99 補到三位數
        ns=str(n);ns='0'*(3-len(ns))+ns 
        s=s+int(ns[i:i+1])**3      
    if s==n: print(ns ,"是阿姆斯壯數")


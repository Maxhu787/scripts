# 用泰勒級數計算圓周率
# π=2x(1+1/3+2/5+3/7+4/9+5/11+.........)

import math # 因為最下面一行有呼叫 math.pi， 所以要先導入 math 套件

def pi(a):
    x=2 ; z=2 ; a=1 ; b=3 ; e=1e-15 # 數值設定
    
    while(z>e):     # 收斂到小數以後的15位，當z> 10 15次繼續執行運算
        z = z*a/b   # 計算每一次要累加的數字  
        x=x+z       # 數字累加    
        a=a+1       # 分子每次加 1
        b=b+2       # 分母每次加 2
    return x        # 程式終止後x會傳進 pi

print(pi(0))        # 印出 pi 的數值
print(math.pi)      # 這是 math 函數印出來的pi



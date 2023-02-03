# 度數的三角函數 
import math                   # 要使用三角函數必須先引入 math 套件

def dsin(theta):              # 自訂副程式 dsin(theta) 引數是度數
    a=math.pi/(180/theta)     # 在這裡把度數轉成徑度
    return math.sin(a)        # 傳回數值直接從 math 三角函數值傳回即可

print('Sin(30)=',dsin(30))
print('Sin(45)=',dsin(45))
print('Sin(60)=',dsin(60))

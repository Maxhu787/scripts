#  計算正五角形面積

'''
deg = 30 #  數入角度
三角函數之間的關係：
1) sin x = cos (90°- x) 
2) cos x = sin (90°- x)

pi 用泰勒級數展開 = pi(0)
'''

def tylorsin(deg):
    # x=(3.14159*deg)/180
    x=(pi(0)*deg)/180
    s=x
    fc=1
    for i in range(1,20): # 到第 9 已經收斂
        fc=fc*(2*i)*(2*i+1)
        s=s+((-1)**i)*(x**(2*i+1))/fc
        # print(i,fc,s)
        return s

def pi(a):
    x=2;z=2;a=1;b=3;e=1e-15
    while(z>e):
        z = z*a/b
        x=x+z
        a=a+1
        b=b+2
    return x 
print(pi(0))

area= 5* tylorsin(36)*tylorsin(54)
print(' 五角形面積=',area)

# parea=5*math.sin(math.pi*36/180)*math.cos(math.pi*36/180)
# print(parea)

import math
def area(r):
    a=math.pi*r**2
    return a

def volume(r):
    v=(4.0/3.0)*math.pi * r**3
    return v

r=int(input('輸入半徑='))

print('半徑為','r ' ,'的圓面積為:', area(r))
print('半徑為','r ' ,'的球體積為:', volume(r))





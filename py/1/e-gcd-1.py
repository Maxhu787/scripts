# 求GCD (輾轉相除法)

# 可以試 x=546 ; y=429  or x=9 ; y=24  

x=12; y=18

if (x>y):
    x,y = y,x
    
m=x; x=y
while(m>0):
    y=x ; x=m ; m=y % x

print(x)
    

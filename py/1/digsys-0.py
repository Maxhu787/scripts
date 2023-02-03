#十進制轉其他進制
dec = 17
print("十進制:",dec)

# 轉二進制
n=dec
b=''
if ( n<2) :
    b=str(n)
while ( n > 1) :
    b=str(n%2)+b
    n= n//2
    if ( n==1) :
       b=str(n)+b
print("二進制=",b)  

# 轉八進制
n=dec
o=''
if ( n<8) :
    o=str(n)
while ( n > 7) :
    o=str(n%8)+o
    n= n//8
    if ( n<8) :
       o=str(n)+o
print("八進制=",o)

# 轉十六進制
n=dec
x=''
hex='0123456789ABCDEF'
if (n<16) :
    # 要取 n % 16 的餘數,這個字元在 hex 字串的第(餘數)的位置的字元
    x=hex[(n%16):(n%16)+1]    
while ( n > 15) :
    x=hex[n%16:(n % 16 )+1]+x   
    n= n//16
    if ( n<16) : 
       x=hex[(n%16):(n%16)+1]+x  
print("十六進制=",x)

    

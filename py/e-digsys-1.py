#十進制轉其他進制
# http://www.chwa.com.tw/tresource/vs/book1/ch2/2-5.htm

def numsys(dec,ns):
    n=dec
    x=''
    hstr='0123456789ABCDEF'
    if ( n == 0 ) :
        x='0'
    while ( n > 0 ):
        # 要取n % 16的餘數，這個字元在hst字串的第(餘數)的位置的字元
        x=hstr[(n % ns):(n % ns)+1]+x
        n= n//ns
    return x

dec = 18
print("十進制:",dec,":")
print("二進制=",numsys(dec,2))
print("八進制=",numsys(dec,8))
print("十六進制=",numsys(dec,16))

#十進制含小數轉二進制(到小數點後十位)
dec = 12.875
print("十進制=",dec)

n=int(dec); b=''
while ( n > 0) :
    b=str(n%2)+b
    n= n//2

f=dec-int(dec); fb=''
while (len(fb) < 10 and f!=0):
    fb=fb+str(int(f*2))
    f=(f*2)-int(f*2)
    print(f)
    
print("二進制=",b+"."+fb)

    
    


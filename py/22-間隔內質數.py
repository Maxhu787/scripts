low = 2
up = 100

print(low,"至",up," 間隔內的所有質數:")
 
for n in range(low, up + 1):
    f=0 ; i=2
    while( f==0 and i<=((n)/2) ):    # 可以用   i<=((n)//2))   
        if ( n % i )==0:             # 也可以用 i<=((n)//**0.5))
            f=1
        i=i+1    
    if (f==0):
        print( n, "is prime")
        



#1050305-5

def f(n,c):
    sum=0
    if n < 2 : return 0
    
    print("n=",n);print("c=",c,end='') ; print("   執行次數=", c+n)
    for i in range(1,n+1):
        sum =sum + i
        c += 1
    n=int(2*n/3)   # 執行 n * 2 /3 次
    
    sum += f(n,c)  
    
    return sum

#main
f(1000,0)

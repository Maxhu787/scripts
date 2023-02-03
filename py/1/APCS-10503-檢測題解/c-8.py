#1050305-8

a,b=0,1
N=10

for i in range(2,N+1):
    temp=b
    # 費氏數列 1 2 3 5 8 13 21 34 55
    b=a+b                      
    a=temp
    print("%d" %b,end=" ")





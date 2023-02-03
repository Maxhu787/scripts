#1050305-6

def f(n):
    c=0
    sum=0
    if n<2 : return 0
    for i in range(1,n+1):
        c += 1
        sum =sum + i
    sum += f(int(2*n/3))
    return sum


f(1000)


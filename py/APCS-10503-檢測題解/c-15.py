#1050305-15

def f(n,c):
    c += 1
    print("%d\n    -count%d"  %(n,c))
    while (n  !=  1):
        c += 1
        if ((n%2)==1):
            n=3*n + 1
        else:
            n= n/2
        print("%d\n    -count%d"  %(n,c))

#main
f(22,0)




#1050305-15

def f(n,c):
    # c += 1
    print("%2d %2d %2d"  %(c,n,n%2))
    while (n  !=  1):
        c += 1
        print("%2d %2d %2d"  %(c,n,n%2),end="")
        if ((n%2)==1):
            n=3*n + 1
        else:
            n= n/2
        print(" %2d"  % (n))

#main
f(22,0)




#1050305-20

def fun(n):
    fac = 1
    if (n>0):
        fac=n *fun(n-1)
    return fac


print(fun(5))






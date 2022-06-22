#1050305-12

def f1(m):
    print("F1()")
    if (m>3):
        print("f1-> %d\n"  %m)
        return
    else:
        print("f1-> %d\n"  %m)
        f2(m+2)
        print("f1-> %d\n"  %m)

def f2(n):
    print("F2()")
    if (n>3):
        print("f2-> %d\n"  %n)
        return
    else:
        print("f2-> %d\n"  %n)
        f1(n-1)
        print("f2-> %d\n"  %n)

#main
f1(1)


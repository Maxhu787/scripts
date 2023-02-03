#1050305-10

def g(a):
    if (a>1):
        print("g(",a-2,")+3=",g(a-2)+3)
        return g(a-2)+3
    # print(a)
    return a

print("g(13)=",g(13))



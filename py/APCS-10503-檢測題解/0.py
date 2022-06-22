#1050305-7

def a(n,m):
    if (n<10):
        if (m<10):
            return n+m
        else:
            return a(n,m-2)+m
    else:
        print("a(n-1,m)+",n)
        return a(n-1,m)+n

#main
print("a(13,15)函式回傳值為 ",a(13,15))
print("a(12,15)函式回傳值為 ",a(12,15))
print("a(11,15)函式回傳值為 ",a(11,15))
print("a(10,15)函式回傳值為 ",a(10,15))
print("a(9,15)函式回傳值為 ",a(9,15))
print("a(9,13)函式回傳值為 ",a(9,13))
print("a(9,11)函式回傳值為 ",a(9,11))
print("a(9,9)函式回傳值為 ",a(9,9))

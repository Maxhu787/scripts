a, b = 0, 1
print(a,b,end=' ')

for i in range (15):
    c=a+b
    print(c, end=' ')
    a,b=b,c
    

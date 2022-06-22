# While 印出費氏數列 ( 正確 )

a, b = 0, 1
print(a,b,end=' ')
n=1000

while  a+b < n:
    c=a+b
    print(c, end=' ')
    a = b
    b = c           
print()


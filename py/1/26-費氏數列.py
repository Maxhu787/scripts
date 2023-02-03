# 最簡單的費氏數列

n1 = 0 ; n2 = 1
print(n1,end=' ')
for i in range(1,17):
    print(n2,end=' ')
    n=n2
    n2=n1+n2
    n1=n


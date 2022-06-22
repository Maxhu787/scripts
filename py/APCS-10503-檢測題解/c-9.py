#1050305-9

A=[]
B=[]
for i in range(5):
    A.append(0) ; B.append(0)
    A[i] = 2 + i*4   
    B[i] = i*5
    

c=0
for i in range(1,5):
    if (B[i] > A[i]):
        c = c + (B[i] % A[i])
    else:
        c=1
    print(i,c)

print(A[1:5])
print(B[1:5])

print("%d\n" %c)





#1050305-13

i=76 ; j=48
while ((i%j) != 0):
    print(i,j,i%j)
    k=i % j
    i=j
    j=k

print("%d\n"  %j)




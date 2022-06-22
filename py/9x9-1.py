# 九九乘表
for i in range(1,10):
    for j in range (1,10):
        print ("%3d" %(i*j) , end='')
    print()

    
print("\n\n\n")



print(" j=  1  2  3  4  5  6  7  8  9")
print(" -----------------------------")
for i in range(1,10):
    print("%2d=" %i,end='')
    for j in range (1,10):
        print ("%3d" %(i*j) , end='')
    print()

for i in range(1,10):
    for j in range (1,10):  
        print (i*j , end=' ')
    print()
print()

for i in range(1,10):
    for j in range (1,10):  
        print (i*j , end=' ')
    print(end ='\n')
print()

for i in range(1,10):
    for j in range (1,10):
        print ("%3d" %(i*j) , end='')
    print()
print()

for i in range(1,10):
    for j in range (1,10):  
        if i*j < 10 :
            print ('', i*j, end=' ')
        else :       
            print (i*j , end=' ')
    print(end ='\n')
print()

for i in range(1,10):
    for j in range (1,10):  
       if i*j < 10 :
           print (i,'x',j,'= ',i*j, end=' ')
       else :      
           print (i,'x',j,'=',i*j , end=' ')
    print()
print()

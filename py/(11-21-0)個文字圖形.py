for i in range(-4,5):
    print(' '*abs(i), end='')
    for j in range(5-abs(i)):
        print('* ', end='')
    print()

print()
for i in range(-4,5):
    print(' '*abs(i), end='')
    if abs(i)==4 :
        print('*')
    else:
        for j in range(5-abs(i)):
            print('$ ', end='')
        print()
print()

for i in range(-4,5):
    print(' '*abs(i), end='')
    if abs(i)==4 :
        print('*')
    else:
        for j in range(5-abs(i)):
            if abs(i) % 2 == 1:
                print('1 ', end='')
            else:
                print( chr(65)+' ', end='')
        print()
print()

for i in range(-4,5):
    print(' '*abs(i), end='')
    if abs(i)==4 :
        print('*')
    else:
        for j in range(5-abs(i)):
            if abs(i) % 2 == 1:
                print('1 ', end='')
            else:
                print(chr(66-abs(j-1))+' ', end='')
        print()
print()

for i in range(-4,5):
    print(' '*abs(i), end='')
    if abs(i)==4 :
        print('*')        
    else:
        if i == 0 :
            print('* * 0 * *')
        else:    
            for j in range(5-abs(i)):
                if abs(i) % 2 == 1:
                    m=1-(abs(i)//2)
                    w=int(abs(j-m-0.5))
                    print(chr(49+w)+' ', end='')
                else:
                    print(chr(66-abs(j-1))+' ', end='')
            print()
print()

for i in range(-4,5):
    print(' '*abs(i), end='')
    if abs(i)==4 :
        print('*')        
    else:
   
        for j in range(5-abs(i)):
            if abs(i) % 2 == 1:
                m=1-(abs(i)//2)
                w=int(abs(j-m-0.5))
                print(chr(49+w)+' ', end='')
            else:
                ww=66-abs(j-1)
                if i == 0 :
                    if j !=2 :
                        ww=42
                    else:
                        ww=48
                print(chr(ww)+' ', end='')
        print()
print()

for i in range(-4,5):
    print(' '*abs(i), end='')
    if abs(i)==4 :
        print('*')        
    else:
   
        for j in range(5-abs(i)):
            if abs(i) % 2 == 1:
                m=1-(abs(i)//2)
                w=int(abs(j-m-0.5))
                print(chr(49+w)+' ', end='')
            else:
                ww=66-abs(j-1)
                if i == 0 :
                   ww=42 * ( j != 2)
                   if j ==2 : ww = 48
                print(chr(ww)+' ', end='')
        print()
print()


for i in range(-4,5):
    print(' '*abs(i), end='')
    if abs(i)==4 :
        print('*')        
    else:   
        for j in range(5-abs(i)):
            if abs(i) % 2 == 1:
                m=1-(abs(i)//2)
                w=int(abs(j-m-0.5))
                print(chr(49+w)+' ', end='')
            else:
                ww=66-abs(j-1)
                if i == 0 :
                   ww=42 * int( j !=  2) + 48*int(j==2)
                print(chr(ww)+' ', end='')
        print()
print()

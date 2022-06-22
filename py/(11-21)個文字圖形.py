print(' 21 (難度= 5)')
'''
    * 
   1 1 
  A B A 
 1 2 2 1 
* * 0 * * 
 1 2 2 1 
  A B A 
   1 1 
    *
'''


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
    

print(' 11 (難度= 3) ')
'''

    *         * 

   * *       * * 

  * * *     * * * 

 * * * *   * * * * 

* * * * * * * * * *
'''

for i in range(1,5+1):
    for j in range(1,2+1):
        print((5-i)*' ',end='')
        for k in range(1,i+1):
            print('* ',end='')
        print((5-i)*' ',end='')
    print()
    print()

print('\n') # 題目間跳行

print(' 12 (難度: 2) ')
'''
AAAAA
BBBB
CCC
DD
E 
'''
for i in range(1,5+1):
    for j in range(6-i,0,-1):
        print(chr(i+64),end='')
    print()
    
print('\n') # 題目間跳行

print(' 13 (難度: 2) ')
'''
1
01
101
0101
10101
'''

x=0
for i in range(1,5+1):
    for j in range(i):
        x=1-x
        print(x,end='')
    print()    

print('\n') # 題目間跳行


print(' 14 (難度: 1) ')
'''
01111
20222
33033
44404
55550
'''

for i in range(5):
    for j in range(5):
        if (i==j) :
            print(0,end='')
        else:
            print(i+1,end='')
    print()

print('\n') # 題目間跳行

print(' 15 (難度= 3) ')
'''
    1
   121
  12321
 1234321
123454321
'''
    
for i in range(1,5+1):
    for j in range(-4,4+1):
        if ( i >= abs(j)+1):
            print(i-abs(j),end='')
        else:
            print(' ',end='')
    print()
            
print('\n') # 題目間跳行

print(' 16  (難度= 3) ')
'''

    5
   44
  333
 2222
11111
'''


for i in range(1,5+1):
    for j in range(1,5+1):
        if ((i+j)>=6) :
            print(6-i,end='')
        else:
            print(' ',end='')
    print()


print('\n') # 題目間跳行

print(' 17 (難度= 2) ')
'''
 1
 2  3
 4  5  6
 7  8  9 10
11 12 13 14 15
'''
x=1
for i in range(1,5+1):
    for j in range(1,i+1):
        print('%3d' %(x),end='')
        x=x+1
    print()


print('\n') # 題目間跳行

print(' 18  (難度= 3) ')
'''
ABCDEFEDCBA
ABCDE EDCBA
ABCD   DCBA
ABC     CBA
AB       BA
A         A
'''

for i in range(1,6+1):
    for j in range(-5,5+1):
        if ( i<abs(j)+2):
            print(chr(65+(5-abs(j))),end='')
        else:
            print(' ',end='')  
    print()
    
print('\n') # 題目間跳行

print(' 19 (難度: 1) ')
'''
S
SC
SCH
SCHOO
SCHOOL
'''

str='SCHOOL'
for i in range(6):
    print(str[0:i+1])

print('\n') # 題目間跳行

print(' 20  ( 難度= 3 )')
'''
e       e
 d     d
  c   c
   b b
    a
   b  b
  c    c
 d      d
e        e
'''

for i in range(-4,4+1):
    for j in range(-4,4+1):
        if ( abs(i)==abs(j)):
            print(chr(97+abs(i)),end='')
        else:
            print(' ',end='')
    print()    





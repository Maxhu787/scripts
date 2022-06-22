# 1   (難度: 0)
'''
*
**
***
****
*****
'''

for i in range(5+1):
    for j in range(1,i+1):
        print("*",end='')
    print()

print('\n') # 題目間跳行

        
# 2 (難度: 3)
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''

for i in range(-4,4+1):
    print(abs(i)*' ',end='')
    for j in range(1,5-abs(i)+1):
        print(" *",end='')
    print()

print('\n') # 題目間跳空白行

# 3 (難度: 1)
'''
1
22
333
4444
55555
'''

for i in range(1,5+1):
    for j in range(1,i+1):
        print(i,end='')
    print()

print('\n') # 題目間跳空白行

# 4 (難度: 3)
'''
555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555
'''

for i in range(-4,4+1):
    for j in range(-4, 4+1):
        if ( abs(i) > abs(j)) :
            print(abs(i)+1,end='')
        else:
            print(abs(j)+1,end='')
    print()
    
print('\n') # 題目間跳空白行

# 5 (難度: 1)
'''
A
BB
CCC
DDDD
EEEEE
'''

for i in range(5):
    for j in range(i+1):
        print(chr(65+i),end='')
    print() 

print('\n') # 題目間跳空白行

# 6  (難度: 0)
'''
*
*
*
*
*

*****

1
2
3
4
5

12345

A
B
C
D
E

ABCDE
'''

for i in range(0,5):
    print('*')
print()
 
for i in range(0,5):
    print('*',end='')
print()     
 
for i in range(1,6):
    print(i)
print()
 
for i in range(1,6):
    print(i,end='')
print()
 
for i in range(0,5):
    print(chr(65+i))
print()
 
for i in range(0,5):
    print(chr(65+i),end='')
print()


# 7 (難度: 4)

'''
*
**
***
*  *
** **
******
*  *  *
** ** **
*********
*  *  *  *
** ** ** **
************
'''

for i in range(1,4+1):
    for j in range(1,3+1):
        for k in range(i):
            print(j*'*'+(3-j)*' ',end='')
        print()

print('\n') # 題目間跳空白行    

# 8 (難度: 3)
'''
       * 
      * * 
     *   * 
    *     * 
   *       * 
  *         * 
 *           * 
* * * * * * * *
'''

for i in range(1,8):
    print((8-i)*' '+'*'+(((i-1)*2)-1)*' '+(i>1)*'*')
print((i+1)*'* ')

print('\n') # 題目間跳空白行

# 9-0  (難度: 2)
'''
*********
 ******* 
  *****  
   ***   
    *    
   ***   
  *****  
 ******* 
*********
'''
for i in range(-4,4+1):
    for j in range(-4,4+1):
        if (abs(i)>abs(j)-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()

print('\n') # 題目間跳空白行

# 9-1 (難度: 2)
'''
*       *
**     **
***   ***
**** ****
*********
**** ****
***   ***
**     **
*       *
'''

for i in range(-4,4+1):
    for j in range(-4,4+1):
        if (abs(i) < abs(j)+1):
            print('*',end='')
        else:
            print(' ',end='')
    print()

print('\n') # 題目間跳空白行

# 9-2  ( 難度: 3 )
'''
   432101234
 4 *********
 3 **** ****
 2 ***   ***
 1 **     **
 0 *       *
 1 **     **
 2 ***   ***
 3 **** ****
 4 *********
'''

for i in range(-4,4+1):
    for j in range(-4,4+1):
        if ((abs(i)+abs(j)) < 4 ):
            print(' ',end='')
        else:
            print('*',end='')
    print()

print('\n') # 題目間跳空白行

# 10    ( 難度: 3 )
'''
 9876543210123456789
1********* *********
2 ******** ********
3  ******* *******
4   ****** ******
5    ***** *****
6     **** ****
7      *** ***
8       ** **
9        * *   
'''
for i in range(1,9+1):
    for j in range(-9,9+1):
        if (j==0) or (i > 9-abs(j)):
            print (' ',end='')
        else:
            print('*',end='')
    print()



print(' 22 (難度= 5) ')
'''
*  
** 
***
1  1  
22 22 
333333
A  A  A  
BB BB BB 
CCCCCCCCC
1  2  3  4  
11 22 33 44 
111222333444
1  1  1  1  1  
12 12 12 12 12 
123123123123123
'''

for i in range(1,5+1):
    for j in range(1,3+1):
        for k in range(i):
            if i==1 :
                print(j*'*'+(3-j)*' ',end='')
            if i==2 :
                print(j*str(j)+(3-j)*' ',end='')
            if i==3 :
                print(j*chr(64+j)+(3-j)*' ',end='')
            if i==4 :
                print(j*str(k+1)+(3-j)*' ',end='')
            if i==5 :
                print('123'[0:j]+(3-j)*' ',end='')
        print()

print('\n') # 題目間跳空白行

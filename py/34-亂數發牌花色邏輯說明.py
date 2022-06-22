import random
flower=['H','S','D','C']           # 花色
num=['A','2','3','4','5','6','7','8','9','T','J','Q','K']  #數字
c=[]

for i in range(52):                # 填數字    
    c.append(i) 
    print('%2d' % c[i], end=' ')
print('\n\n')

for i in range(52):                # 產生亂數
    r=random.randint(0,51)
    print(r, end=' ')
print('\n\n')


for i in range(52):                # 印出數字
    print(c[i],end=' ')
print('\n\n')

for i in range(52):                # 13 張下跳
    print('%2d' %i, end=' ')
    if (i+1) % 13 == 0 :
        print()
print('\n\n')

for i in range(52):                # 印花色  數字
    print(c[i]//13,c[i] % 13 , end=' ')
    if (i+1) % 13 == 0 :
        print()
print('\n\n')

for i in range(52):                # 印花色 SHDC 和 數字
    f=c[i]//13
    m=c[i] % 13
    print(flower[f],num[m], end=' ')
    if (i+1) % 13 == 0 :
        print()
print('\n\n')


for i in range(51):                # 印 亂數
    r=random.randint(0,52)
    c[i],c[r]=c[r],c[i]
    print(c[i],end=' ')
print('\n\n')

for i in range(52):                # 印花色， 數字
    f=c[i]//13
    m=c[i] % 13
    print(f,m, end=' ')
    if (i+1) % 13 == 0 :
        print()
print('\n\n')

for i in range(52):                # 印結果
    f=c[i]//13
    m=c[i] % 13
    print(flower[f],num[m], end=' ')
    if (i+1) % 13 == 0 :
        print()
print('\n\n')



       
    


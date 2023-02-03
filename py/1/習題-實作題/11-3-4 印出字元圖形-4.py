# 11-3-4 印出字元圖形-4 ( 重邏輯, 這程式還可以再簡化)
'''
123456789
2       8
3       7
4       6
5       5
6       4
7       3
8       2
987654321
'''

for i in range(9):
    for j in range(9):
        if i==0:        
            print(j+1+i, end='')
        if i>0 and i<8:
            if j >0 and j<8:
                print(' ',end='')
            else:
                print(i+1+(8-2*i)*(j==8), end='')
        if i ==8:
            print(17-j-i, end='')
            
    print()

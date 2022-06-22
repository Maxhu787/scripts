# 奇數魔方陣(二維陣列)

a =int(input("請輸入方陣數值單數(3~15)="))
ary=[ [0] * (a+1) for i in range(a+1) ]
r = 1                    # 定義列的位置
c = int((a + 1) / 2)     # 定義欄的位置
numb = 1                 # 即使放入的數字為 1

ary[c][r]=numb
for i in range(1 , (a * a) ):  # 輸入5，就是5x5方陣
    r = r - 1; c = c + 1 # 往右上方走， r=r-1，c=c+1     
    if (r<1) :           # r<1 超過左邊第一欄位置
        r=a
    if (c>a) :           # c>q 超過上面第一列位置
        c=1
    numb = numb + 1      # 數字放進方格後數字須加一 
    if (ary[c][r] != 0 ): # 如果這個欄位已經有放數字
        c = c - 1; r = r + 2  #開放位置 要放到下面
        if (c<1) :       # 超過左邊第一欄位置
            c=a
        if (r>a):        # 超過右邊欄位
            r=r-a
        ary[c][r] = numb # 數字放進方格
        # print (c, r, numb)
    else:
        ary[c][r] = numb
        # print (c, r, numb)

for i in range(1,a+1):   # 印出結果
    for j in range(1,a+1):
        if ( ary[j][i] < 10 ):
            print( " ",end='')
        print(ary[j][i],end=' ')
    print()

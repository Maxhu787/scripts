# 距陣轉換

def rotate(b):        # 旋轉
    global r,c, ro    # r= 列 、 c= 欄 、 ro 旋轉後的串列
    r,c=c,r           # 2x3 轉 3x2
    ro = [ [0] * c for i in range(r) ]  # 預備空串列  
    for i in range(r):
        for j in range(c):
           ro[i][j] = b[j][r-1-i]
           # print(i,j,j,r-1-i,r)       # 追蹤 旋轉行列值
           # input()
    return

def updown(a):        # 翻轉
    global r,c, usd
    usd=[ [0] * c for i in range(r) ]
    # print(len(a))     # a 列數 r
    # print(len(a[0]))  # a 欄數 c

    for i in range(r):
        for j in range(c):
            usd[i][j]=a[r-1-i][j]   # 行上下對調、列不變
    return  

ip1=input()             # 輸入 R、C、M
listip1=list(map(int,ip1.split()))  # 字串轉數值串列
r=listip1[0]; c=listip1[1]; m=listip1[2] #取得R、C、M數值
z_list=[ [0] * c for i in range(r) ]     # 預備空串列

for i in range(r):      # 有 r 列
    ipline=input()      # 逐行輸入資料
    listipline=list(map(int,ipline.split()))#字串轉數值串列
    z_list[i]=listipline                    #存入每一列
    
ip2=input()             # 輸入 M 的操作代碼 0 旋轉; 1 翻轉     
listip2=list(map(int,ip2.split())) 
count=len(listip2)      # M 的長度

for i in range(count):  # 逐部操作 count-1-i 由後往前推
    if listip2[count-1-i] == 1:             #  1 翻轉
        updown(z_list)           #  送進副程式
        z_list=usd               #  翻轉後的串列 送出
    if listip2[count-1-i] == 0:             #  0 旋轉
        rotate(z_list)           #  送進副程式
        z_list=ro                #  旋轉後的串列 送出

print(r,c)
for i in range(r):               #  串列 轉文字
    for j in range(c):
        print(z_list[i][j],end=' ')
    print()


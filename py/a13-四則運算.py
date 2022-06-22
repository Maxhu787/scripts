# 四則運算 ( 中序式 ) 依序算乘 除 減 加法
# 轉後序式: 23,12,3,*,+,18,-,2,3,*,-8,2,/,+
ip='23+12*3-18-2*3+8/2' ; print(ip)
l=len(ip)          # 字串長度 
for k in range(l): # _ 代替 - 號，避免和負數混淆
    if ip[k]=='-' :
        ip=ip[0:k]+'_'+ip[k+1:l]
opersynb=['*','/','_','+']   # _ 代替 - 號， 避免和負數混淆        
ip=' '+ip+' '                # ip 前後加空白

for pr in range(4):              
    c=ip.count(opersynb[pr]) #  計算: 乘 除 減 加符號各有幾個

l=len(ip)                    #  加後空白ip 字串長度

operator=[];oploc=[] #operator 是找符號;oploc 是找位置
for j in range(l):   #  找運算符號
    if (ip[j]=='+') or (ip[j]=='_') or (ip[j]=='*')  \
       or (ip[j]=='/') or (ip[j]==' '):      # 一行切成兩行 
        operator.append(ip[j])  # 符號串列   
        oploc.append(j)         # 符號位置串列

n=len(operator)                 # 符號串列
numlist=[]
for i in range(n-1):
    numlist.append(int(ip[oploc[i]+1:oploc[i+1]]))
c=len(numlist)
while c>1 :     # 先乘除 , C 是運算元的總個數 
    d=0; i=0    # D是一個指標,i是從第一找到最後一個運算符號 
    while d==0 and i< len(operator) :
        if operator[i] =="*" or operator[i] =="/" :
            if operator[i] =="*":  # 如果找到乘的符號
                numlist[i-1]=numlist[i-1]*numlist[i]
                d=i
            if operator[i] =="/":  # 如果找到乘除的符號
                numlist[i-1]=numlist[i-1]/numlist[i]
                d=i         # D如果不是0，代表有進行過運算
        i=i+1   
    if d!=0:
        del numlist[d:d+1]  # 要從串列中將已經算過的元素刪除
        del operator[d:d+1] # 要從串列中將已經算過的符號刪除
    c=c-1
n=len(operator) # 去除 * / 運算式後運算元
c=len(numlist) 

while c>1 :     # 後加減
    d=0; i=0
    while d==0 and i< len(operator)  :        
        if operator[i] =="+" or operator[i] =="_" :
            if operator[i] =="+":
                numlist[i-1]=numlist[i-1]+numlist[i]
                d=i
            if operator[i] =="_":
                numlist[i-1]=numlist[i-1]-numlist[i]
                d=i
        i=i+1   
    if d!=0:
        del numlist[d:d+1]  # 要從串列中將已經算過的元素刪除
        del operator[d:d+1] # 要從串列中將已經算過的符號刪除
    c=c-1

print("=",numlist[0])       # 印出最後結果


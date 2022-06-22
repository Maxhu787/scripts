# 文字字串轉數字串列
# ipline =input()

ipline='1 10 100 1000 10000' # 輸入的字串
print(ipline)                # 印出輸入的字串

def mymap(ipline):           # mymap 自訂的 map 函數
    ipline=' '+ipline+' '    # 前後先加空白
    strlen=len(ipline); # print(strlen)
    l=0; r=0 ; c=0 ; numlist=[]
    for i in range(strlen):
        # print(ipline[i],end='')
        if ipline[i]==' ':
            # print(i,end=' ')
            l=r ; r=i ; # print(l,r)
            c=c+1 ; # print(c)
            if c>1 :
                numlist.append(int(ipline[l+1:r]))
    return numlist
            
listA=mymap(ipline)
print(listA)

''' 如果要將五行測資轉數字串列  
for i in range(5):
    ipline =input()
    list00=mymap(ipline)
    print(list00)

'''

        
        
   

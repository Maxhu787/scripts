# 四則運算 ( 中序式 ) 依序算乘 除 加 減法 (未處理括號)
ip='23+12*3-18-2*3+8/2' # 測試:'23+12*3-18-2*3-8/2','56*2-78+33/11+14' 
print(ip,"=")
listop1=[];listop2=[]; listop3=[] # 運算子、位數、運算元
l=len(ip); ans=0
for k in range(l):
    if ip[k]=='-' :
        ip=ip[0:k]+'_'+ip[k+1:l]

opersynb=['*','/','+','_']        # _ 代替- 減號， 因怕和負號 - 混淆
ip=' '+ip+' '  

for pr in range(2):               # 先乘除
    # print("pr=",pr)
    c=ip.count(opersynb[pr])      # * / + - 的個數 
    # print('c=',c)
           
    while c > 0 :
        l=len(ip);                # print("l of ip=",l,ip,opersynb[pr])
        operator=[];oploc=[]
        for j in range(l):            
            if (ip[j]=='+') or (ip[j]=='_') or \
               (ip[j]=='*') or (ip[j]=='/') or (ip[j]==' '): # 本行未用
                operator.append(ip[j]);oploc.append(j)
        index=(operator.index(opersynb[pr]))
               
        op1=float(ip[oploc[index-1]+1:oploc[index]])
        op2=float(ip[oploc[index]+1:oploc[index+1]])
        if pr==0: 
            op12=op1*op2
        elif pr==1 :
            op12=op1/op2
#        elif pr==2 :
#            op12=op1+op2
#        elif pr==3 :
#            op12=op1-op2
     
        ip=ip[0:oploc[index-1]+1]+ \
            str(op12)+ip[oploc[index+1]:len(ip)]
        c=ip.count(opersynb[pr])

s=0
for i in range(len(ip)):    # 後加減             
    # print(ip[i:i+1])
    if ip[i:i+1] == '+' or ip[i:i+1] == '_' :
        # print(i,ip[i:i+1])
        listop1.append(ip[i:i+1] )       # 運算子
        listop2.append(i)                # 位數
        listop3.append(float(ip[s+1:i])) # 運算元
        s=i
        # print(listop1,listop2,listop3)
listop3.append(float(ip[s+1:len(ip)]))   # 末位數
# print(listop1,listop2,listop3)

ans=listop3[0]              # 首位數
for j in range(len(listop1)):
    # print(j,listop1[j],listop2[j],listop3[j])
    if listop1[j] =='+' :
        ans=ans+listop3[j+1] 
        # print (ans)
    if listop1[j] =='_':
        ans= ans - listop3[j+1]
        # print (ans)
print(ans)



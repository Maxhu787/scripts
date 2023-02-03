# 四則運算 ( 中序式 ) 依序算乘 除 加 減法
# 轉後序式: 23,12,3,*,+,18,-,2,3,*,-8,2,/,-
ip='23+12*3-18-2*3-8/2' 
ip0='23+12*3-18-2*3+8/2'
l=len(ip)
for k in range(l):
    if ip[k]=='-' :
        ip=ip[0:k]+'_'+ip[k+1:l]
opersynb=['*','/','+','_']
ip=' '+ip+' '  ;  print(ip0)

for pr in range(4):
    c=ip.count(opersynb[pr]) 
           
    while c > 0 :
        l=len(ip)
        operator=[];oploc=[]
        for j in range(l):            
            if (ip[j]=='+') or (ip[j]=='_') or \
               (ip[j]=='*') or (ip[j]=='/') or (ip[j]==' '):
                operator.append(ip[j]);oploc.append(j)
        index=(operator.index(opersynb[pr]))
               
        op1=float(ip[oploc[index-1]+1:oploc[index]])
        op2=float(ip[oploc[index]+1:oploc[index+1]])
        if pr==0: 
            op12=op1*op2
        elif pr==1 :
            op12=op1/op2
        elif pr==2 :
            op12=op1+op2
        elif pr==3 :
            op12=op1-op2
     
        ip=ip[0:oploc[index-1]+1]+ \
            str(op12)+ip[oploc[index+1]:len(ip)]
        c=ip.count(opersynb[pr])

print('=',ip)

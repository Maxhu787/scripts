# 四則運算 ( 中序式 ) 依序算乘 除 減 加法 (一定要先減後加)
# 轉後序式: 23,12,3,*,+,18,-,2,3,*,-8,2,/,+
ip='23+12*3-18-2*3-8/2' ; print(ip)
l=len(ip) 
for k in range(l):
    if ip[k]=='-' :
        ip=ip[0:k]+'_'+ip[k+1:l]
opersynb=['*','/','_','+']   # _ 代替 - 號， 避免和負數混淆
ip=' '+ip+' '                # ip 前後加空白
for pr in range(4):          #  因為有負數，所以一定要先減後加    
    c=ip.count(opersynb[pr]) #  計算: 乘 除 減 加符號各有幾個    

           
    while c > 0 :            #  如果還有 運算符號 
        l=len(ip)            #  ip 字串長度
        operator=[];oploc=[] #operator 是找符號;oploc 是找位置
        for j in range(l):   #  找運算符號         
            if (ip[j]=='+') or (ip[j]=='_') or \
               (ip[j]=='*') or (ip[j]=='/') or (ip[j]==' '):
                operator.append(ip[j]);oploc.append(j)
              
        index=(operator.index(opersynb[pr])) # 正要執行的運算               
        op1=float(ip[oploc[index-1]+1:oploc[index]])#第一位數                   
        op2=float(ip[oploc[index]+1:oploc[index+1]])#第二位數                  
        
        if pr==0:                            # */_+ 分別運算
            op12=op1*op2                     # *
        elif pr==1 :                          
            op12=op1/op2                     # /
        elif pr==2 :
            op12=op1-op2                     # -
        elif pr==3 :
            op12=op1+op2                     # +
    
        ip=ip[0:oploc[index-1]+1]+ \
            str(op12)+ip[oploc[index+1]:len(ip)]   # 執行運算 
        c=ip.count(opersynb[pr])             # 結果

print('=',ip)
    

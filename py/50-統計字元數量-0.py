# 飆程式網  #1012 ( 離線題解 )
n=5
iplist=["0","00","5140514", "9999999999","1234567890"]
nc=[]
for i in range(10):
    nc.append(0)

for i in range(n):
    str=iplist[i]
    print(iplist[i],end=' ')
    for j in range(len(str)):
        nc[int(str[j:j+1])]= nc[int(str[j:j+1])]+1
   
    for k in range(10):
        print(nc[k],end=' ')
        nc[k]=0
    print()

    


            
                   

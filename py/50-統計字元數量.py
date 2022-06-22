# 飆程式網  #1012 ( 離線題解 )
n=5
iplist=["0","00","5140514", \
        "9999999999","1234567890"]
for i in range(n):
    print(iplist[i],end=' ')
    for j in range(10):
        c=iplist[i].count(str(j))
        print(c,end=' ')
        c=0           
    print()

# 10-5-2-2 奇數字元的字串
strline="jerome"
iplist=list(strline)
print(iplist)

for i in iplist[1::2]:   # 從第一個開始增量 = 2    
    print(i,end='')
    

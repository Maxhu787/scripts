# ipline =input()
# 
ipline='3 7 1586 9 8'
print(ipline)
strlen=len(ipline)

iplist=list(ipline)        # 先字串轉串列， 限定轉換一位
lenlist=ipline.count(' ')

for i in range(strlen):
    if iplist[i] != ' ':
        iplist[i]=int(iplist[i])

leniplist=len(iplist)
for i in range(leniplist-2):
    if iplist[i] != ' ':
        c=i
        while iplist[c+1] != ' ':
            iplist[i]=int(iplist[i])*10+int(iplist[c+1])
            c=c+1

newiplist=iplist
for i in range(12):
    if iplist[i]==' ':
        c=i+1 
        while c< 12 and iplist[c] != ' ' :
            if (c-i) >1 :
                newiplist[c:c+1]=' '
            c=c+1

lennewiplist=len(newiplist)
for i in range(lennewiplist-1,0,-1):
    if newiplist[i]==' ':
        del newiplist[i]
        
print(newiplist)


# 計算行列的和
iplist=['3 5','1 2 3 4 5','2 4 6 8 10','3 6 9 12 15']
list01=list(map(int,iplist[0].split())) ;   print(list01)
m=int(list01[0]); n=int(list01[1])

listsum=[]
for c in range(n):
    listsum.append(0)
print(listsum)

for i in range(1,m+1):
    ipline=iplist[i]; # print(ipline)
    list02=list(map(int,ipline.split())) ; # print(list02)
    for ii in range(n):
        listsum[ii]=listsum[ii]+list02[ii]
    # print(listsum)
    sum=0
    for j in range(n):
        sum=sum+list02[j]        
    print(sum)
# print(listsum)
for p in range(n):
    print(listsum[p],end=' ')

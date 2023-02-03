# Read in data & 計算行列的和
iplist=['5 6','1 2 3 4 5 6','2 4 6 8 12 14','3 5 7 9 11 13','6 5 4 3 2 1','1 10 100 1000 10000 100000']
list01=list(map(int,iplist[0].split())) ; #  print(list01)

n=int(list01[0]); m=int(list01[1])
listsum=[]
for c in range(m):
    listsum.append(0)
# print(listsum)

for i in range(1,n+1):
    ipline=iplist[i]; #  print(ipline)
    list02=list(map(int,ipline.split())) ; # print(list02)
    for ii in range(m):
        listsum[ii]=listsum[ii]+list02[ii]
    # print(listsum)
    sum=0
    for j in range(m):
        sum=sum+list02[j]        
    print(sum)
# print(listsum)
for p in range(m):
    if p==(m-1) :
        print(listsum[p])
    else:  
        print(listsum[p],end=' ')




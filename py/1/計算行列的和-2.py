# 計算行列的和

ipline=input()
list01=list(map(int,ipline.split())) ;# print(list01)
n=int(list01[0]); m=int(list01[1])

listsum=[]
for c in range(m):
    listsum.append(0)
# print(listsum)

for i in range(1,n+1):
    ipline=input(); #  print(ipline)
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




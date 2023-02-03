# 1050305APCS實作題---題三

#輸入--------------
n=int(input("請輸入線段數量："))

node=[]
for i in range(n):
    x,y=input("請輸入線段之左右座標：").split(" ")
    x=int(x);y=int(y)
    node.append([x,y])


#處理--------------
node.sort()                   #按照線段的左邊排序
nl=node[0][0]; nr=node[0][1]
ans=0

for i in range(1,n):
    tl=node[i][0]; tr=node[i][1]
    if (tl>nr):                 #新的左邊比現在的右邊大 --> 新線段
        ans=ans+(nr-nl)         #覆蓋線段長度累加
        nl=tl; nr=tr            #指定新的左右邊
    elif (tl<=nr and tr>nr):
        nr=tr                   #線段重覆或相鄰

ans=ans+(nr-nl)                 #最後一段覆蓋線段長度累加

#輸出--------------    
print("線段覆蓋長度為 ",ans)










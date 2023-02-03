# 巴斯卡三角形(一維串列) 使用二個串列
list01=[];list02=[]
for i in range(15):
    list01.append(0)
    list02.append(0)
list01[1]=1
print(list01[1:2])
c=0

while c< 10 :
    for i in range(15):
        list02[i]=list01[i-1]+list01[i]

    # list01=list02 使用同一位置(* 這裡不能用* )
    for i in range(15):
        list01[i]=list02[i]    # 使用不同位置
    
    c=c+1
    print(list02[1:c+2]) 




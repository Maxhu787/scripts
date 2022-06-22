# 費氏數列 ( 串列 )
list01=[]
for i in range(17):
    list01.append(0)
list01[1]=1
c=1
print(list01)
while c<16:
    a=list01[c-1]+list01[c]
    list01[c+1]=a
    print(list01)
    c=c+1

    

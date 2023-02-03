# 9-6-2-2 各種硬幣最少的數量

listm   = [50,10,5,1]
listcoin= []

m=int(input("票價="))

print("各種硬幣最少的數量=")
for i in range(3):
    listcoin.append(m//listm[i])
    m=m-listm[i]*listcoin[i]
    print(listm[i],"元", listcoin[i],"個")
    
listcoin.append(m)
print(listm[3],"元", listcoin[3],"個")



    



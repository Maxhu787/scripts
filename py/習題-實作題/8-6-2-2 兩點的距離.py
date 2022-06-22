# 8-6-2-2 輸入兩點座標-輸出兩點的距離
a=1;b=1
c=5;d=5

def distance(a,b,c,d): 
    dis=((a-c)**2+(b-d)**2)**0.5
    dis=int(dis*100)/100   # 小數取二位
    return dis

print(distance(a,b,c,d))

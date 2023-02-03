# ipline=['3 5','1 2 3 4 5','2 4 6 8 10','3 6 9 12 15']
# 如果這個程式要離線執行，資料請手動從鍵盤輸入資料
ipline=input()            # 從鍵盤輸入資料
list01=list(map(int,ipline.split()))
num=list01[0]
print(num)
iplist=[]
for i in range(num):
    list01=list(map(int,input().split()))  # 從鍵盤輸入資料 
    print(list01)
    iplist.append(list01)
print(iplist)

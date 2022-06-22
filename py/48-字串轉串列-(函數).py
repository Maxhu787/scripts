# 48-字串串列互轉-(函數).py
# ipline=input()                  # 讀取檢測系統用這一行

ipline='1 10 100 1000 10000'      # 上船時這一行要拿掉
print(ipline)                     # 印出輸入字串
def Convert(string):              # 字串轉陣列副程式
    list1 = list(string.split(" ")) 
    return list1 
numlist=Convert(ipline)
print(numlist)                    # 列出陣列





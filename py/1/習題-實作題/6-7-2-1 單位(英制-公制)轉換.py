# 6-7-2-1 單位(英制-公制)轉換
print("單位轉換:")
print("1. 公制 -> 英制")
print("2. 英制 -> 公制")
a=input("請輸入 (1 或 2) :")
print(a)

if a=="1":
    cm=float(input("請輸入幾公分 :"))
    inch=cm/2.54
    ft=inch/12
    print(cm, "公分=",ft,"英呎=",inch,"英吋")
elif a=="2":
    inch=float(input("請輸入幾英吋 :"))
    cm=inch*2.54
    print(inch, "英吋=",cm,"公分")
else :
    print("輸入錯誤")
    
    

#  判別迴文

i_str = 'aIbohPhoBiA'   # 輸入字串
slen=len(i_str)         # 算字串長度
i_str=i_str.lower()     # 字串改成小寫

flag=True                # 檢查旗標先設為 '真' True
 
for i in range(slen//2 ):  # 從第一個字開始到中間檢查每一字元
   #從兩邊開始到中間檢查每一字元列印字元
   print (i_str[i:i+1], i_str[slen-i-1:slen-i]) 
   if  (i_str[i:i+1] != i_str[slen-i-1:slen-i]) :
      flag = false       # 如果有一個字不同 旗標設為 '假' False

if (flag):
   print("字串是迴文")   # 旗標為 '真' True
else:
   print("字串不是迴文") # 旗標設為 '假' False


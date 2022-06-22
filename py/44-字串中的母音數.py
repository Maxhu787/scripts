# 字中的母音數

v = 'aeiou' # 母音
i_str = 'Practice makes perfect.'
i_str = i_str.casefold()  # 轉小寫
print(i_str)

c = {}.fromkeys(v,0)   # fromkeys() 函數用於創建一個新字典
print(c)  # 印出 這個新字典， 計數都還是零

for char in i_str:
   if char in c:
       c[char] =  c[char] + 1  # 計算字中的母音數
print(c)

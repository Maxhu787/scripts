# 刪除標點符號

# 定義標點符號
p = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

ip_str = "Hello!!!, I am ---a handsome boy."

# 設定一空字串
str = ""
for char in ip_str:  # 字串從第一個字到最後一個字
   if char not in p: # 檢查字元是否 不 在 p 字串中?
       str = str + char # 如果 不 在 p 字串中 就加入 str 字串

print(str)           # 已刪除標點符號

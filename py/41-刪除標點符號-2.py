# 刪除標點符號

# 定義標點符號
p = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

i_str = "Hello!!!, I am ---a handsome boy."

# 設定一空字串
str = ""
for i in range(0,len(i_str)-1):  # 字串從第一個字到最後一個字
    char=(i_str[i:i+1])
    print(char, end='')           # 可以檢視每一個字元
    if char not in p:             # 檢查字元是否 不 在 p 字串中?
        str = str + char          # 如果 不 在 p 字串中 就加入 str 字串
print()
print(str)                        # 已刪除標點符號



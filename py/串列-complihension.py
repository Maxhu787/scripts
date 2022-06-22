# 文字串列轉成文字字串
list00 = [0,1,2,3,4,5,6,7,8,9]
print(list00)

list01 = [str(x) for x in list00]   # 字串串列
print(list01)

print(" ".join(list01))         # 字串串列轉字串

for s in list01:
    print(s,end=' ')         # 字串串列轉字串
print()

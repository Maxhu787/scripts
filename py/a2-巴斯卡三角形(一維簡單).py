# 巴斯卡三角形(一維簡單) 很神奇的推導方式
# 從後面往前推，不會有競態條件（Race Condition）的問題
n = int(input("幾層: "))
plist = []

for i in range(1, n + 1):
    plist.append(1)  # 串列第一個元素都是一

    for j in range(i - 2, 0, -1):  # 從右到左
        # print(i,j,plist[j],plist[j-1],end='')
        plist[j]= plist[j] + plist[j - 1]  # 回推
        # print(plist)

    print("行號:", i, plist)

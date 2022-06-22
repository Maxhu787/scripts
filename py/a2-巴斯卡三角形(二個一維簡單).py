n = int(input("幾層? "))        # 使用二個一維串列
left= [1]                       # 串列第一個元素都是一
for i in range(n):
    print("行號:", i + 1, left)
    plist = []
    plist.append(left[0])
    for i in range(len(left) - 1):
        plist.append(left[i] + left[i+1])
    plist.append(left[-1])
    left = plist
    

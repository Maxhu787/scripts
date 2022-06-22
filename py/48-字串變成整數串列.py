# 字串變成整數串列
ipline='3 27 1586 93 688'
list=ipline.split(' ') # 將編號用空白分開
print(list)

w=[int(x) for x in list] # 將輸入的字串變成整數串列
print(w)

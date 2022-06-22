# 單字按字母順序排列

# 設定字串
i_str = "Genius is one percent inspiration and ninety-nine percent perspiration. "

w = i_str.split() # 句子拆成串列
print('串列個數=',len(w))

print(w) # 印出未排序單字串列

for i in range(len(w)):    # 串列排序
   for j in range(i+1,len(w)):
      if ( w[i] < w[j] ):  # 由大到小
         temp=w[i] ; w[i]=w[j] ; w[j]=temp  # 交換 

i=1
for w1 in w:
   print(i,w1) # 印出排序單字串列 
   i=i+1

w.sort() # 串列排序  由小到大 (很好用的函數)
print(w) # 印出單字串列 
print()  # 印空白行

print("依ASCII排序的單字:")
for w2 in w:
   print(w2)

   

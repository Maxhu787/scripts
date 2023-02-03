# 單字按字母順序排列

ip_str = "Genius is one percent inspiration and ninety-nine percent perspiration. "

w = ip_str.split() # 句子拆成串列

print(w) # 印出未排序單字串列

w.sort() # 串列排序 (很好用的函數

print(w) # 印出單字串列 

print("依ASCII排序的單字:")
for word in w:
   print(word)

   

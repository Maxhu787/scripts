# 開檔讀檔寫檔
'''
開啟兩個檔案 ipfile-1.txt 和 ipfile.txt 取出文字檔的內容，
前面加上 hello送到 1234567890.txt的檔案之中
'''

# 開檔 定義 ipfile-1.txt 為 file_1
with open("ipfile-1.txt",'r',encoding = 'utf-8') as file_1:
    c1 = file_1.read()

# 印出 檔案內容
for i in range(len(c1)+1):
    print(c1[i:i+1],end='')
print()

# Close opend file
file_1.close()
    
with open("ipfile-1.txt",'r',encoding = 'utf-8') as file_1:
    for i in range(0,len(c1)+1):
        a = file_1.read(1)
        print(a,end='')
    print()
# Close opend file
file_1.close()

 
## 開檔
fp = open('factorial.txt', "r")
line = fp.readline()
 
## 用 while 逐行讀取檔案內容，直至檔案結尾
while line:
    print(line,end='')
    line = fp.readline()
 
fp.close()
    




# 開檔  讀檔
# 開啟檔案 ipfile-1.txt 取出文字檔的內容，


# 開檔 定義 ipfile-1.txt 為 file_1
with open("ipfile-1.txt",'r',encoding = 'utf-8') as file_1:
    c1 = file_1.read() # c1='0123456789'   一次讀完    

# 印出 檔案內容 一字一字印出
for i in range(len(c1)+1):
    print(c1[i:i+1],end='')
print()
    
# 關檔
file_1.close()






    


    


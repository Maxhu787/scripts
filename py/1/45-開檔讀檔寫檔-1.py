# 開檔讀檔寫檔
'''
開啟兩個檔案 ipfile-1.txt 和 ipfile.txt 取出文字檔的內容，
前面加上 hello送到 1234567890.txt的檔案之中
'''

# 開檔 定義 ipfile-1.txt 為 file_1
with open("ipfile-1.txt",'r',encoding = 'utf-8') as file_1:

   # 開檔 定義 ipfile-2.txt 為 file_2
   with open("ipfile-2.txt",'r',encoding = 'utf-8') as file_2:
   
       # 讀入 ipfile-2.txt 檔案內容放在 c2 = 'abcdefghij'
       c2 = file_2.read()

       # 讀入 ipfile-1.txt 檔案內容放在 c1 = '1234567890' 
       for c1 in file_1:
           # t = 'Hello 1234567890abcdefghij'
           t = "Hello "+ c1 + c2

           # 建立 1234567890.txt 定義為 new_file, 將 t 放入 new_file
           with open(c1.strip()+".txt",'w',encoding = 'utf-8') as new_file:
               new_file.write(t)
print('檔案順利建立並寫入!')


# 關檔
file_1.close()
file_2.close()

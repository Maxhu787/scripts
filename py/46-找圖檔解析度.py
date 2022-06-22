# 找圖檔解析度
# JPEG(JFIF)交換格式 請上網查詢


def jpeg_res(filename):
   
   # 以二進制模式讀取 jpeg 檔案
   with open(filename,'rb') as img_file:

       # image（2個字節）位於第164位
       img_file.seek(163)

       # 讀取2個字節
       a = img_file.read(2)

       # 計算高度: 放在 a[164]~ a[165]
       # << 左移動運算符：a[0] << 8  是將a[0] 運算數的各二進位全部左移8 位，
       # 由 << 右邊的數字指定了移動的位數，高位丟棄，低位補0。
       # 等於乘上 128，其實就是  a[0] =高位元 + a[1] = 低位元 的內涵值
       height = (a[0] << 8) + a[1]

       # 2個字節是寬度
       a = img_file.read(2)

       # 計算寬度:  放在 a[166]~ a[167]
       width = (a[0] << 8) + a[1]

   print("JPEG 圖檔解析度=",width,"x",height)

jpeg_res("img1.jpeg")  # 一定要 JPEG 文件交換格式（JFIF）標準
                       # 如果是 jpg 處理不一定正確，可以到線上轉換格式 
                       # jpg 轉成jpeg, https://www.freefileconvert.com/

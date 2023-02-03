# 計算檔案長度和SHA1安全哈希算法
'''
sha1加密: 
 
SHA1的全稱是Secure Hash Algorithm(安全哈希算法) 。 SHA1基於MD5，加密後的數據長度更長，
它對長度小於264的輸入，產生長度為160bit的散列值。比MD5多32位。
因此，比MD5更加安全，但SHA1的運算速度就比MD5要慢了。
 
1. 需要匯入hashlib 模組：
https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/364973/
 
2. 線上sha1/sha224/sha256/sha384/sha512加密工具
http://tools.jb51.net/password/sha_encode

3. hash算法的用途
https://www.twblogs.net/a/5b8ec7822b7177188347aec2/zh-cn
'''
 
# 呼叫 hashlib 套件
import hashlib
 
# 此函數返回SHA-1哈希值
def hash_file(filename):
 
   # 從 sha1 函數 取值
   h = hashlib.sha1()
 
   # 打開檔案，以二進制模式讀取
   with open(filename,'rb') as file:
 
       # 循環直到檔案結束
       chunk = 0 ; n=0
       while chunk != b'':
           # 每次讀進 1024 位元
           chunk = file.read(1024)
           h.update(chunk)
           n=n+1
       print(' 檔案長度=',n-1,'k')
       print(' 檔案結束碼=',chunk)
 
   # 回傳加密後的16 進位數字
   return h.hexdigest()
 
message = hash_file("demo.mp3")
print(message)

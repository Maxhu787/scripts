# 遞迴算二進位
 
def bin(n):
    if n > 1:
        bin(n//2)
    print(n % 2,end = '')
   
# 輸入進位數
dec = 18
bin(dec)

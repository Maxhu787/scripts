#  判別迴文

ip_str = 'aIbohPhoBiA' # 輸入字串

ip_str = ip_str.casefold() # 字串改成小寫

rev_str = reversed(ip_str) # 字串反轉

if list(ip_str) == list(rev_str):
   print("字串是迴文")
else:
   print("字串不是迴文")

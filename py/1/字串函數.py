# 這是註解
""" 這是字串，同時也是註解，使用三個雙引號 """
""" 
這是字串，同時也是註解，使用三個雙引號，可以跨行註解。
用在字串上可以保留縮排、空格，也可以拿來使用，如輸出 print()
"""

# 註解 ( 是字串，同時也是註解 )
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。"""
print (para_str)

# 字元&字串
s = "Hello Python"
print(s)      # prints whole string
print(s[0])   # prints "H"
print(s[1])   # prints "e"
 
# 複製字串  
# strcpy(sStr1,sStr)   
sStr= 'strcpy'   
sStr = sStr  
sStr= 'strcpy'   
print(sStr)  
 
# 接字串  
# strcat(sStr1,sStr)   
sStr= 'strcat'   
sStr = 'append'   
sStr+= sStr   
print(sStr) 

# 取子字串
var1 = 'Hello World!'
var2 = "Runoob" 
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

# 串接字串
var1 = 'Hello World!' 
print ("已更新字符串 : ", var1[:6] + 'Python!')

# 設定字串格式
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))


# 設定子字串文字
s = "Hello Python" 
print(s + ' ' + s) # print concatenated string.
print(s.replace('Hello','Thanks')) # print a string with a replaced word

# 字串轉數值
v1 = int('123')
print( v1+123)

# 數值轉字串
v=123
print(str(v)+'abc')

 
# 換大寫
s = s.upper()
print(s)
 
# 換小寫
s = s.lower()
print(s)

# 比較 包含 字串
sentence = "The cat is brown"
q = "cat" 
if q == sentence:
    print('strings equal') 
if q in sentence:
    print(q + " found in " + sentence)

# 特殊的字串 (分行 斷行)
str1 = "In Python,\nyou can use special characters in strings.\nThese special characters can be..."
print(str1)

# 判断字串值是否相等
a="hello"
b="hello"
print(a==b,id(a)==id(b))


# 去空格及特殊符號
# s.strip() .lstrip() .rstrip(',')
s="    Ilove you!   "
print(s.lstrip())
print(s.rstrip())














    




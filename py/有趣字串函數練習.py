# captalize() 函数 (将一个字符串的第一个字母大写)
str = "hello world!"
print ("str.capitalize(): ", str.capitalize())


# center(width, fillchar) 函数 将字符串居中，居中后的长度为 width
str = "hello world!"
print ("str.center(20): ", str.center(20))
print ("str.center(20,'-'): ", str.center(20,'-'))

# 字串資料可以是以單引號（'）或雙引號（"）包起來的 文字資料 ，相對於數值資料，字串就是用來表示文字的資料。

# count(str, start=0, end=len(string)) 函数 返回该字符串中出现某字符串序列（或字符）的次数
str = "hello world! hello world!"
sub = "o"
print ("str.count(sub): ", str.count(sub))
sub = "hello"
print ("str.count(sub, 5) ", str.count(sub, 5))

# len(string) 函数 得到该字符串的长度
str = "Hello world!"
print ("the length of str: ", len(str))

# ljust(width, fillchar=’ ‘)函数 在字符串的右边填充字符使得字符串达到指定长度
str = "Hello world"
print ( str.ljust(15))
print (str.ljust(15,'!'))

# 複製指定長度的字元
#strncpy(sStr1,sStr2,n)
sStr1 = ''
sStr2 = '12345'
n = 3
sStr1 = sStr2[0:n]
print ( sStr1)


# 翻轉字串
#strrev(sStr1)
sStr1 = 'abcdefg'
sStr1 = sStr1[::-1]
print (sStr1)

# 擷取字串
str = '0123456789'
print (str[0:3]) #擷取第一位到第三位的字元
print (str[:]) #擷取字串的全部字元
print (str[6:]) #擷取第七個字元到結尾
print (str[:-3]) #擷取從頭開始到倒數第三個字元之前
print (str[2]) #擷取第三個字元
print (str[-1]) #擷取倒數第一個字元
print (str[::-1]) #創造一個與原字串順序相反的字串
print (str[-3:-1]) #擷取倒數第三位與倒數第一位之前的字元
print (str[-3:]) #擷取倒數第三位到結尾
print (str[:-5:-3]) #逆序擷取

# 输入字符
# c = input("请输入一个字符: ")
c='A'
# 输入ASCII码，并将输入的数字转为整型
# a = int(input("请输入一个ASCII码: "))
a=65
print( c + " 的ASCII 码为", ord(c))
print( a , " 对应的字符为", chr(a))

# 產生重複字串
x = 'Cat'
y='K'
b=' '
print(x*3)
print(y*5)
print('A'+b*5+'B')


# Unicode 字串
x = u'Hi,\u0020Eric'
print (x)


# List 資料 List 裡的資料可以是任何資料型態 使用中括號（ [ 及 ] ）包起來
a = [1, 3, 'abc', 7, "xyz"]
print (a[3])
print (a[1:3])



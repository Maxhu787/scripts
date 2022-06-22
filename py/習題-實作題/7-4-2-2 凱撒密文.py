# 7-4-2-2 凱撒密文  (值得思考)
str="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("原始字串=",str)
n=int(input(" 請輸入(整數) n= ")); n=n % 26
for i in range(len(str)):
    strmove=chr((ord(str[i:i+1])+n)%90 +1)
    # print(chr(ord(str[i:i+1])+n),end="")
# print()

for i in range(len(str)):
    if (ord(str[i:i+1])+n) > 90 : # Z 以後的字母 變成 A
        strmove= chr(((ord(str[i:i+1])+n) % 91) + 65)
    else :
        strmove=chr((ord(str[i:i+1])+n))
    print(strmove,end='')
    

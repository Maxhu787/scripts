#  身份證檢核(字典)
dict1={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":34,\
      "J":18,"K":19,"L":20,"M":21,"N":22,"O":35,"P":23,"Q":24,"R":25,\
      "S":26,"T":27,"U":28,"V":29,"W":32,"X":30,"Y":31,"Z":33}
# print("字典內容:"+str(dict1))

id='A123456789'

sum=0
n=int(dict1[id[0:1]])
sum=n//10+(n%10)*9

for i in range(1,8+1):
    sum=sum+(9-i)*int(id[i:i+1])
check=int(id[9:10])
if (((sum+check)% 10 )==0):
    print(id,'的身分證號碼正確!')
else:
    print(id,'的身分證號碼不正確!')

print('身分證的檢查碼=', check)











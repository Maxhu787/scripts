#  身份證檢核(串列)

alph=[10,11,12,13,14,15,16,17,34,18,19,20,21,22,35,23,24,25,26,27,28,29,32,30,31,32,33]
# print("串列元素:",alph)

str='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

id='A123456789'
indx=str.find(id[0:1])

sum=0

n=alph[indx]
sum=n//10+(n%10)*9

for i in range(1,8+1):
    sum=sum+(9-i)*int(id[i:i+1])
check=int(id[9:10])
if (((sum+check)% 10 )==0):
    print(id,'的身分證號碼正確!')
else:
    print(id,'的身分證號碼不正確!')

print('身分證的檢查碼=', check)

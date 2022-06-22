# 一個簡單的計算器，可以使用函數'''進行加，減，乘和除'''

# 函數: 兩個數字相加
def add(x, y):
   return x + y

# 函數: 兩個數字相減
def subtract(x, y):
   return x - y

# 函數: 兩個數字相乘
def multiply(x, y):
   return x * y

# 函數: 兩個數字相除
def divide(x, y):
   return x / y

print("選擇操作:")
print("1.相加")
print("2.相減")
print("3.相乘")
print("4.相除")

# 選擇計算方式 
choice = input("選擇計算方式(1/2/3/4):")

num1 = int(input("輸入第一個數字: "))
num2 = int(input("輸入第二個數字: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("輸入錯誤")

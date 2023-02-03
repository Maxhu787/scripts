#  找數字的因數
 
def factor(x):
    print(x,"的因數有:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i, end=' ')
 
num = 240
factor(num)

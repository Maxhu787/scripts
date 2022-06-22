# 函數 印出費氏數列 (執行函數)

def fib(n):
    a, b = 0, 1
    while a < n :
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(1000) # 印出 小於 1000 以前的 費氏數

# -----------( 只有主程式 )----------------

n=1000
a, b = 0, 1
while a < n :
    print(a, end=' ')
    a, b = b, a+b
print()

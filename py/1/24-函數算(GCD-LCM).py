# 計算 gcd, lcm 

def gcd(m, n):  # 最簡潔的  gcd 函數
    return m if n == 0 else gcd(n, m % n)

def lcm(m, n):
    return m * n // gcd(m, n)
    
m = 56
n = 24

print(m,"&",n ,"的 GCD= ", gcd(m, n))
print(m,"&",n ,"的 LCM= ", lcm(m, n))

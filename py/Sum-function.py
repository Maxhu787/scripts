# 函數呼叫說明
def sum(n):        # 用def 定義函數名稱 sum
    s=0
    for i in range(s,n+1):
        s=s+i
    return s       # 會把 s 送到 sum 再傳回主程式

print(sum(100))    # 在主程式中呼叫  sum() 函數

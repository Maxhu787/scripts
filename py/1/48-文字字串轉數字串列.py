# 文字字串轉數字串列
# ipline =input()
ipline='3 27 1586 93 688'# 輸入的字串
ipline=' '+ipline+' '    # 前後先加空白

print(ipline)            # 印出輸入的字串

numlist=[]               # 設定空串列
strlen=len(ipline)
c=0 ; l=0;  r=0     # 設定初值

for i in range(strlen):
    if ipline[i]==' ':   # 找出空白位置
        l=r; r=i         # left 的 l 是每個數值字串 左邊位置
        c=c+1            # c 累加數值到串列中的計數器  
        if c>1 :
            numlist.append(int(ipline[l+1:r]))  # 累加數值到串列
print(numlist)           # 印出串列

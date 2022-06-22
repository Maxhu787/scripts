# 巴斯卡三角形 (一維串列)

def pascal(n):                             # 有二個串列 p & row
    if n <= 0:
        return 
    else:
        row = [1]
        for i in range(n):
            print(row)                     # 印出 row
            p = row[:]                     # p 代表前一列, p = row 結果一樣
            for j in range(1, len(row)):        
                row[j] = p[j] + p[j-1]
            row.append(1)                  # 用附加 (append) 比較不佔空間
pascal(10)

# 10-5-2-1 找到陣列的最大值
# 一般語言所稱的陣列(Array) 在Python稱為串列(List)

def arrayMax(listb):
    big=0
    for i in listb:
        if i> big : big=i
    return big

ipline="18 23 3 14 5"
# ipline=input()    # 手動輸入資料
lista = list(map(int, ipline.split(' ')))
# print(lista)

print(arrayMax(lista))

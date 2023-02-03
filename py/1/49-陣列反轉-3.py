# 陣列反轉 (飆程式網 #1011) - 3
n=5
ipline="2 3 12 4 5"
# n=int(input())
# ipline = input()
lista = list(map(int, ipline.split(' ')))
lista.reverse()
# print(lista)
print(' '.join(map(str,lista)))

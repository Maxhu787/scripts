# 交換兩個變數

x = 5 ; y = 10
print(' x 交換前: {}'.format(x))
print(' y 交換前: {}'.format(y))
print()

temp = x ; x = y ; y = temp  #  Python 有一特殊的交換方法: x,y = y,x

print(' x 交換後: {}'.format(x))
print(' y 交換後: {}'.format(y))

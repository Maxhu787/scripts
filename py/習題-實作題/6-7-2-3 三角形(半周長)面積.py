# 6-7-2-3  計算三角形三邊長度的一半(半周長)，併計算三角形的面積面積
'''
計算半周長
s = ( a + b + c ) / 2 
計算面積
area= ( s * ( s - a ) * ( s - b ) * ( s - c ) ) ** 0.5
'''

a = float ( input ( ' 輸入三角形第一邊長: ' ) ) 
b = float ( input ( ' 輸入三角形第二邊長: ' ) ) 
c = float ( input ( ' 輸入三角形第三邊長: ' ) ) 
#計算半周長
s = ( a + b + c ) / 2 
#計算面積
area= ( s * ( s - a ) * ( s - b ) * ( s - c ) ) ** 0.5 
print ( ' 三角形面積為%0.2f ' % area )

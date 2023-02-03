# (練習: 2-14)   
op=input('輸入運算符號( + - * / :')      # 顯性輸入
a=int(input('整數-1:  '))
b=int(input('整數-2:  '))

if op == ('+'):
	print(a+b)
elif op == ('-'):
	print(a-b)
elif op == ('*'):
	print(a*b)
elif op == ('/'):
	print(a/b)
else:
	print('輸入錯誤')

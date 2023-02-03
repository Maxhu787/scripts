a = ['Jerome', 0.38, 1234, True] 
for i in range(0, len(a)):
    print (a[i],type(a[i]))

print ('變數是string的有：')
for i in range(0,len(a)):
    # 變數的 class 類型判斷，可以用 isinstance()
    if isinstance(a[i], str):
        print (a[i], type(a[i])) 

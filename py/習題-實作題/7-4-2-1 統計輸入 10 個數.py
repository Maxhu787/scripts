# 7-4-2-1 統計輸入 10 個數 (值得看)
import random
listr=[]; listrsort=[]
for i in range(1,10):
    listr.append(random.randint(1,100))
print("1. 原始串列=",listr)

listori=listr     # 原始複製串列 不能更動
listcopy=listr[:] # 複製串列 可以更動

'''
***** 串列 複製 *****
python中直接通過等號賦值實際上只是引用地址的傳遞
如：
a = [1,2,3,4,5]
b=a
當a的值改變時，b的值也會隨之改變

如果希望b和a沒有關係，可以通過下面的方法


a = [1,2,3,4,5]
b=a[:]
這樣a和b就是兩個完全獨立的陣列，互相不會影響
'''

print("2. 原始複製串列=",listori)
print("3. 複製串列=",listcopy,"\n")

listr.sort(); print("4. 正向排序串列=",listr)
listr.sort(reverse=True); print("5. 反向排序串列=",listr,"\n")
    
avg=sum(listr)/len(listr); print("6. 平均(浮點)數=", avg)
print("7. 平均(整數)數= {:.2f} ".format(avg)) # 取2位小數

print("8. 大於平均(整數)數=",end=' ' )
for i in range(len(listr)):
    if listr[i] > avg : print(listr[i],end=' ' )
print("\n")

print("9. 複製串列=",listcopy,"\n")  # 不能用 listori 實際上只是引用地址的傳遞

n=len(listcopy)
for i in range(n):
    for j in range(i+1,n):
        if listcopy[i] > listcopy[j]:
            listcopy[i] , listcopy[j] =  listcopy[j],listcopy[i]

print("10. 氣泡正向排序串列=",listcopy)


            
        
    




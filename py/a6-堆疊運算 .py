# 堆疊運算 

def menu():
    print("請輸入選項( 0 結束)：")
    print("(1)插入值至堆疊")
    print("(2)顯示堆疊前端")
    print("(3)刪除前端值")
    print("(4)顯示所有內容")
    return

list=[1,2,3,4,5]
print('堆疊值=',list,"\n")
menu()

s= int(input("(0-4):"))
while (s != 0):
    if (s==1):
        add=int(input("插入值="))
        list.insert(0,add)
        print('堆疊值=',list)
    elif (s==2) :
        print(list[0])
    elif (s==3):
        list.remove(list[0])
        print('堆疊值=',list)
    elif (s==4):    
        print('堆疊值=',list)
    s= int(input("(0-4):"))
          
      

#輸出如下圖 1050305-1
'''
    *
   ***
  *****
 *******
*********

原印

    *
   **
  ***
 ****
*****

'''


k=4
m=1
for i in range(1,6):
    for j in range(1,k+1):
        print(" ",end="")

    for j in range(0,2*(m-1)+1): # 也可以只改這一行  
        print("*",end="")

    print("\n")
    k=k-1
    m=m+1  # m=m+1 改 m=m+2 , 橫行累加印出
    
    

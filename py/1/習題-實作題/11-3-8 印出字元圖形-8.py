# 11-3-8 印出字元圖形-8
'''
         *         
        * *        
       *   *       
* * * * * * * * * *
 *   *       *   * 
  * *         * *  
   *           *   
  * *         * *  
 *   *       *   * 
* * * * * * * * * *
       *   *       
        * *        
         *
'''         
for x in range(0,13):
    for y in range(0,19):
        if (abs(x-6)==3 and y%2==0) or abs(x-y+3)==6 or abs(x+y-15)==6:
            print("*",end='')
        else:
            print(" ",end='')
    print()

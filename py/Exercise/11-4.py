for i in range(-2,3):
    print(" "*abs(i), end='')
    for j in range(2-abs(i)+1):        
        print("* ",end='')
    print()    

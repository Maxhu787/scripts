for i in range(1,1000):
    d1=i//100
    d2=(i//10) % 10
    d3= i %10
    # print(i,d1,d2,d3)
    if (i ==d1**3+d2**3+d3**3):
        print( i)

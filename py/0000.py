for i in range(100,1000):
    a1=i//100
    a2=(i //10) % 10
    a3= i % 10
    if (a1**3+a2**3+a3**3)==i:
        print(i)

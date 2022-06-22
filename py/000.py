t0 = time.time()

for a in range(0,10):
    for b in range(0,10):
        for c in range( 0,10):
            res=a**3+b**3+c**3
            dignum=int(str(a)+str(b)+str(c))
            if (res == dignum and res>10**2) :
                print(res)

t1 = time.time()
print("費時:",t1-t0) ; print("\n\n")

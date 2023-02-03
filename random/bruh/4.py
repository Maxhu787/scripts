max = int(input("Max: "))
a, b = 0, 1

while a < max:
    print(a, end=' ')
    a, b = b, a+b
print("\n")

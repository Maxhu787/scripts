fruits = {"apple", "banana", "cherry"}
print(fruits)

for x in fruits:
    print(x)

fruits.add("orange")
print(fruits)

fruits.update(["orange", "mango", "grapes"])
print(fruits)

print(len(fruits))

fruits.remove("banana")
print(fruits)

x = fruits.pop()
print(x)
print(fruits)


fruits.clear()
print(fruits)


fruits = {"apple", "banana", "cherry"}
print(fruits)
del fruits
# print(fruits)

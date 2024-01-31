product = 1
for i in reversed(range(1,101)):
    product = product * i
    print(product)

total = 0
for i in map(int, str(product)):
    total += i
    print (total)

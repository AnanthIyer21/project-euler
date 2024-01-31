absolutetotal = 0
for i in range(2,10000000):
    total = 0
    for j in map(int,str(i)):
        total += j**5
    if total == i:
        absolutetotal += i
print(absolutetotal)

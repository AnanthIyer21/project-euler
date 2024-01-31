longest = 0
value = 0
for i in range(1,1000):
    x = 1/i
    total = 0
    for j in map(int,str(x)):
        total += 1
    if total > longest:
        longest = total
        value = i
print(value)
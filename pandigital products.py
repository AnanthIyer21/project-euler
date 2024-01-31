def pandigital(x, y):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    total = 0
    for i in map(int, str(x)):
        if i in numbers:
            numbers.remove(i)
    for j in map(int, str(y)):
        if j in numbers:
            numbers.remove(j)
    for k in map(int, str(x * y)):
        if k in numbers:
            numbers.remove(k)
    for l in numbers:
        total += 1
    if total == 0:
        return True


list_of_numbers = []
smth = 0
for i in range(1, 2000):
    for j in range(1, 2000):
        if pandigital(i, j) == True:
            if i * j in list_of_numbers:
                smth += 1
            else:
                list_of_numbers.append(i * j)

total = 0
for k in list_of_numbers:
    total += k

print(total)

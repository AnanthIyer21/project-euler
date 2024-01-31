sth = 0
list_of_numbers = []
for a in range(2, 101):
    for b in range(2, 101):
        if a ** b in list_of_numbers:
            sth += 1
        else:
            list_of_numbers.append(a**b)

total = 0
for i in list_of_numbers:
    total += 1

print(list_of_numbers)
print(total)

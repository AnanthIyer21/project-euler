def find_reversed(x):
    num = x
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num


total = 0
for i in range(1,1000000000):
    hehe = 0
    smtjh = find_reversed(i) + i
    for j in map(int,str(smtjh)):
        if j % 2 == 0:
            hehe += 1
    if hehe == 0:
        total += 1
print(total)
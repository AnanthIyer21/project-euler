#1st jan 1901 was a tuesday
days = 2
count = 0
for years in range(1901, 2001):
    for months in range(1,13):
        if months == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            days += 31
        elif months == 4 or 6 or 9 or 11:
            days += 30
        elif months == 2 and years % 4 != 0:
            days += 28
        elif months == 2 and years % 4 == 0:
            days += 29

        if days % 7 == 0:
            count += 1

print(count)


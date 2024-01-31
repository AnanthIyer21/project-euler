def amicable (x):
    total = 0
    total2 = 0
    for i in range(1,int(x/2)+1):
        if x % i == 0:
            total += i
    if x != total:
        for j in range(1,int(total/2)+1):
            if total % j == 0:
                total2 += j
        if total2 == x:
            return True

listofnum = 0
for i in range(1,10001):
    if amicable(i) == True:
        listofnum += i
        print(listofnum)

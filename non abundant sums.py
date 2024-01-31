import math
def abundant(x):
    stuff = [1]
    smth = 0
    for i in range(2,int(math.sqrt(x))+1):
        if x % i ==0:
            stuff.append(i)
            stuff.append(int(x/i))
    for j in stuff:
        smth += j
    if smth > x:
        return False

total = 0
for i in range(1,28124):
    blah = 0
    for j in range(1,i+1):
        if abundant(j) == True and abundant(i-j) == True:
            blah += 1
            break
    if blah > 0:
        total += i

print(total)

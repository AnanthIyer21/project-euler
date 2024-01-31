num_of_digits = 0
first = 1
second = 1
third = 0
index = 0
while num_of_digits < 1000:
    num_of_digits = 0
    for i in map(int,str(first)):
        num_of_digits += 1
    third = first+second
    first=second
    second=third
    index += 1

print(index)

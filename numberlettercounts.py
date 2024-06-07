ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

largestring = ''
for i in range(1,1001):
    if i < 20:
        largestring += ones[i-1]
    elif 20 <= i < 100:
        if i % 10 == 0:
            largestring += tens[int(i/10)-2]
        elif i % 10 != 0:
            largestring = largestring + tens[int((i-(i%10))/10)-2] + ones[(i%10)-1]
    elif 100 <= i < 1000:
        if i % 100 == 0:
            largestring = largestring + ones[int(i/100)-1] + 'hundred'
        elif 0 < i % 100 < 20 :
            largestring = largestring + ones[int((i-(i%100))/100)-1] + 'hundredand' + ones[(i%100)-1]
        elif i % 100 >= 20:
            if (i % 100) % 10 == 0:
                largestring = largestring + ones[int((i-(i%100))/100)-1] + 'hundredand' + tens[(int((i % 100)/10))-2]
            elif (i % 100) % 10 != 0:
                largestring = largestring + ones[int((i-(i%100))/100)-1] + 'hundredand' + tens[int(((i%100)-((i%100)%10))/10)-2] + ones[((i%100)%10)-1]
    elif i == 1000:
        largestring += 'onethousand'

number_of_characters = 0

for j in largestring:
    number_of_characters += 1
print(number_of_characters)
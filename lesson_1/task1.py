numbers = input().split()
sum = 0
for number in numbers:
    if float(number).is_integer():
        sum += int(number)
    else:
        sum += float(number)
print(sum)

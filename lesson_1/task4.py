numbers = input().split()
squares = 0
for num in numbers:
    num = float(num)
    squares += num ** 2
print(squares)

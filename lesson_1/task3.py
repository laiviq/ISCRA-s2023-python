numbers = input().split()
result = ""
for num in numbers:
    num = float(num)
    result += str(abs(int(num))) + " "
print(result.strip())

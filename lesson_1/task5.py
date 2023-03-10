text = input().replace(" ", "")
key = int(input())
new_text = "".join([chr((ord(c) - 97 + key) % 26 + 97) for c in text])
print(new_text)


text = input()
while True:
    try:
        rule = input().split("->")
        text = text.replace(rule[0], rule[1])
        print(text)
    except:
        break

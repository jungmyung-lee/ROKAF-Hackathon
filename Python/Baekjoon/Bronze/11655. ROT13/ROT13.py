S = input()
s = ""

for i in S:
    if i == " ":
        s += i
        continue
    elif i.isupper():
        result = (ord(i)-65) + 13
        if result > 25:
            result -= 26
            s += chr(result+65)
        else:
            s += chr(result+65)
    elif i.islower():
        result = (ord(i)-97) + 13
        if result > 25:
            result -= 26
            s += chr(result+97)
        else:
            s += chr(result+97)
    else:
        s += i
print(s)

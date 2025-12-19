S = input()
s = ""

for char in S:
    if char == " ":
        s += char
        continue
    elif char.isupper():
        result = (ord(char)-65) + 13
        if result > 25:
            result -= 26
            s += chr(result+65)
        else:
            s += chr(result+65)
    elif char.islower():
        result = (ord(char)-97) + 13
        if result > 25:
            result -= 26
            s += chr(result+97)
        else:
            s += chr(result+97)
    else:
        s += char
print(s)

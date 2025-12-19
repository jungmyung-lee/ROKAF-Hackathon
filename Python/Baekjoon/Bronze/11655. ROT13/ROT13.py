ROT_SHIFT = 13
ALPHABET_SIZE = 26
UPPER_A = ord("A")
LOWER_A = ord("a")

S = input()
s = ""

for char in S:
    if char.isalpha():
        base = UPPER_A if char.isupper() else LOWER_A
        offset = (ord(char) - base + ROT_SHIFT) % ALPHABET_SIZE
        s += chr(base + offset)
    else:
        s += char
print(s)

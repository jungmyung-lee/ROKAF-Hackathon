S = list(input().split())
a = S[0]
b = S[1]

a = a[::-1]
b = b[::-1]

if a>b:
    print(a)
else:
    print(b)
    
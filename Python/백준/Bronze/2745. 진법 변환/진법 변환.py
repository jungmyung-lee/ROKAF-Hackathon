A = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = 0

N, B = input().split()
B = int(B)

for i, k in enumerate(N[::-1]):
    total += B ** i * A.index(k)
    
print(total)
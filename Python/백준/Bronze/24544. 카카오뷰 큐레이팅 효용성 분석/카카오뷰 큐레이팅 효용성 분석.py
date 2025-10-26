n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
total = 0
for i in range(len(B)):
    if B[i] == 0:
        total += A[i]
print(sum(A))
print(total)


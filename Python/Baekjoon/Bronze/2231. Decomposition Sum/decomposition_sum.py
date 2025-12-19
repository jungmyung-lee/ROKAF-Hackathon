N = int(input())

for i in range(1, N+1):
    sum1 = sum(list(map(int ,str(i))))
    total = sum1 + i
    if total == N:
        print(i)
        break
    if i == N:
        print(0)
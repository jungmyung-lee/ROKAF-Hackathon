n = int(input())
A = list(map(int, input().split()))

dp = [1] * n

dp[0] = 1
for i in range(1, n):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)
                
print(max(dp))
a = max(dp)
ans = []

for i in range(n-1, -1, -1):
    if dp[i] == a:
        ans.append(A[i])
        a -= 1

ans = ans[::-1]
for i in ans:
    print(i, end= " ")
    

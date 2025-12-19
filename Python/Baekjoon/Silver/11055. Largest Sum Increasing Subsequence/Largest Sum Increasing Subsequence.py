n = int(input())
A = list(map(int, input().split()))
    
dp = [1] * n
dp[0] = A[0]

for i in range(1, n):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[j] + A[i], dp[i])
        else:
            dp[i] = max(A[i], dp[i])
                
print(max(dp))
n = int(input())
A = list(map(int, input().split()))
dp=[[x for x in A] for i in range(2)]

for i in range(1,n):
    dp[0][i] = max(dp[0][i-1] + A[i], A[i])
    dp[1][i] = max(dp[1][i-1] + A[i], dp[0][i-1])
         

print(max( max(dp[0]), max(dp[1]) ))


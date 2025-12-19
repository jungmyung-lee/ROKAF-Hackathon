n = int(input())
dp = [[1] * 10 for i in range(1001)]

dp[0] = [1,1,1,1,1,1,1,1,1,1]

for i in range(1, 1001):
    for j in range(10):
        if j == 0:
            dp[i][0] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
print(sum(dp[n-1]) % 10007)
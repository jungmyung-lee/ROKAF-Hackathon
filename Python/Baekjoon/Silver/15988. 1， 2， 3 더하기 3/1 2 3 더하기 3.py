n = int(input())
dp = [1] * 1000001

dp[0] = 1
dp[1] = 2
dp[2] = 4
for i in range(3, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009
    
for i in range(n):
    k = int(input())
    print(dp[k-1] % 1000000009 )
        
    
        
n = int(input())
g =[]
dp = [[1000] * 3 for i in range(n)]
    
for i in range(n):
    row= list(map(int, input().split()))
    g.append(row)
        
dp[0] = [g[0][0], g[0][1], g[0][2]]      
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + g[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + g[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + g[i][2]
    
print(min(dp[n-1]))
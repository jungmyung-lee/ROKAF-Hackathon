import sys
input = sys.stdin.readline

n = int(input())
p =[]
for i in range(n):
    row = list(map(int, input().split() ))
    p.append(row)
    
ans = 10000001

for j in range(3):
    dp = [ [1001] * 3 for i in range(n)]
    dp[0][j] = p[0][j]
    for i in range(1,n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + p[i][0]   
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + p[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + p[i][2]
    dp[n-1][j] = 10000001
    ans = min(ans, min(dp[n-1]))
    
print(ans)
    
    
    



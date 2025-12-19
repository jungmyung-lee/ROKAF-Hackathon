n = int(input())




for i in range(n):
    k = int(input())
        
    graph = []
    dp = [[0] * k for i in range(2)]
    
    for i in range(2):
        a = list(map(int, input().split()))
        graph.append(a)
            
    dp[0][0] = graph[0][0]
    dp[1][0] = graph[1][0]
    if k>= 2:
        dp[0][1] = graph[1][0] + graph[0][1]
        dp[1][1] = graph[0][0] + graph[1][1]

    for i in range(2, k):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) +graph[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) +graph[1][i]
            
    print(max(dp[0][k-1],dp[1][k-1]))
    
    
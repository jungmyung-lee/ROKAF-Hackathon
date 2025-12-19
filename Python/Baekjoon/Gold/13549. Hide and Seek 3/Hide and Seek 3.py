from collections import deque

graph = [0] * 100001
visited = [False] * 100001

def bfs(x):
    visited[x] = True
    q = deque([x])
    
    while q:
        x = q.popleft()
        if x == k:
            print(graph[x])
            break
        
        # 순간이동 먼저 처리 (0초)
        nx = 2 * x
        if 0 <= nx <= 100000 and not visited[nx]:
            visited[nx] = True
            graph[nx] = graph[x]
            q.appendleft(nx)

        # x - 1 이동 (1초)
        nx = x - 1
        if 0 <= nx <= 100000 and not visited[nx]:
            visited[nx] = True
            graph[nx] = graph[x] + 1
            q.append(nx)
        
        # x + 1 이동 (1초)
        nx = x + 1
        if 0 <= nx <= 100000 and not visited[nx]:
            visited[nx] = True
            graph[nx] = graph[x] + 1
            q.append(nx)

n, k = map(int, input().split())
bfs(n)
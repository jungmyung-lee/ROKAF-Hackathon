from collections import deque
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs(x):
    visited[x] = True
    q = deque([x])

    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)



n,m = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
    
for i in range(m):
    a,b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1
        
print(cnt)

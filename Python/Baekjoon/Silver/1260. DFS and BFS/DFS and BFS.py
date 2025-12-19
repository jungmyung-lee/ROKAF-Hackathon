from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)



    
def bfs(x):
    visited[x] = True
    q = deque([x])
    
    while q:
        x = q.popleft()
        print(x, end= " ")
        for i in sorted(graph[x]):
            if not visited[i]:
                visited[i] = True
                q.append(i)
    
def dfs(x):
    visited[x] = True
    print(x, end=" ")
    
    for i in sorted(graph[x]):
        if not visited[i]:
            dfs(i)
                
                
n,m,v = map(int, input().split())

visited= [False] * (n+1)
graph= [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
        
dfs(v)
print()
visited= [False] * (n+1)
bfs(v)
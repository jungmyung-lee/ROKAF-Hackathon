import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int, input().split())
    
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
ans = []
    
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
        
def bfs(x):
    visited[x] =True
    q = deque([x])
    
    while q:
        x = q.popleft()
        global cnt
        cnt += 1
        
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                    
            
                
                    
for i in range(1,n+1):
    cnt = 0
    if not visited[i]:
        bfs(i)
        ans.append(cnt)
            
total = 1            
for i in ans:
    total *= i
    
print(total%1000000007)
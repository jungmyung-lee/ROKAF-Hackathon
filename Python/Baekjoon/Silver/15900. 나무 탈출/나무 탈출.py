from collections import deque
import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(start, depth):
    visited[start] = True
    arrive = True
    global result
    
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth+1)
            arrive = False
    
    if arrive:
        result += depth
        return
            
    
    
                
n = int(input())
visited = [False] * (n+1)
graph= [ [] for i in range(n+1)]


for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
dfs(1, 0)
    
if result % 2 ==0:
    print("No")
else:
    print("Yes")



    
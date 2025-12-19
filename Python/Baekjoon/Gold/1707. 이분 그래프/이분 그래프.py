from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def bfs(x,color):
    global result
    visited[x] = True
    q= deque([[x,color]])
    
    while q:
        x,color = q.popleft()
        
        for i in graph[x]:
            if color == color_list[i]:
                
                result = True
                return
                
            if not visited[i]:
                visited[i] = True
                color_list[i] = -color
                q.append([i,-color])
                



k= int(input())


for i in range(k):
    v,e = map(int, input().split())
    visited = [False] * (v+1)
    color_list = [0] * (v+1)
    graph = [[] for i in range(v+1)]
    
    result = False
    for i in range(e):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
            
    for i in range(1,v+1):
        if not visited[i]:
            bfs(i,1)
            
    if result:
        print("NO")
    else:
        print("YES")
            
    
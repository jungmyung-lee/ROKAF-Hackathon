from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
    
dx= [1,-1,0,0]
dy=[0,0,1,-1]
    
def bfs(x,y):
    graph[x][y] = 0
    q = deque([[x,y]])
        
    while q:
        x,y = q.popleft()
        cnt = graph[x][y]
        
        if x== n-1 and y == m-1 :
            return cnt
                
        for i in range(4):
            nx = x+ dx[i]
            ny = y +dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx,ny])
                    
    return cnt

graph = []
n, m = map(int, input().split())
for i in range(n):
    row = list(map(int, input().strip()))
    graph.append(row)
        
print(bfs(0,0) +1)
    

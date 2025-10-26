from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append([i,j])
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] +1
                q.append([nx,ny])
    
        

result = True 
graph=[]
cnt_list = []
m,n = map(int, input().split())
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


bfs()
ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit()
        ans = max(ans, graph[i][j])
        
            
print(ans-1)
            



    
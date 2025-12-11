from collections import deque

dx = [1,-1,2,-2,2,-2,1,-1]
dy = [-2,-2, -1,-1,1,1,2,2]    
def bfs(start_x, start_y, target_x, target_y):
    q = deque([[start_x, start_y]])
    graph[start_x][start_y] = 1
        
    while q:

        x,y= q.popleft()
        if x==target_x and y==target_y:
            return(graph[x][y] -1)
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=k or ny<0 or ny>=k:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] +1
                q.append([nx,ny])  
                    
                
t = int(input())
                    
for i in range(t):
    k = int(input())
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
        
    graph= []    
        
    for i in range(k):
        row = [0] * k
        graph.append(row)
            
        
    ans = bfs(x1,y1,x2,y2)
    print(ans)
            
        
       
        
            
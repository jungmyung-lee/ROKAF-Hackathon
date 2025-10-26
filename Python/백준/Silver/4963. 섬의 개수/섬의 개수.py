import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

graph = []
    
dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]
    
def dfs(x,y):
    if x<0 or x>=h or y<0 or y>= w:
        return False
        
    if graph[x][y] == 1:
        graph[x][y] = 0
            
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
    return False

    

        

result = 0
while True:
    w,h= list(map(int, input().split()))
    if w ==0 and h ==0:
        break
    
    for i in range(h):
        row = list(map(int, input().split()))
        graph.append(row)
        
    for i in range(h):
        for j in range(w):
            if dfs(i,j) == True:
                result += 1
                
    
    print(result)
    graph=[]
    result =0
    
        
        
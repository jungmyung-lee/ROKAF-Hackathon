graph = []
num = []

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y):
    if x<0 or x>= n or y<0 or y>= n:
        return False
    
    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx,ny)
        return True
    return False

n = int(input())
for i in range(n):
    row = list(map(int, input()))
    graph.append(row)

cnt = 0
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            num.append(cnt)
            cnt = 0

num.sort()
print(len(num))
for i in num:
    print(i)
    
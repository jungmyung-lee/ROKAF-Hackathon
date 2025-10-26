from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


    
def bfs(x):
    q=deque([x])
    
    while q:
        x = q.popleft()
        if x == k:
            return graph[x]
        
        for nx in [2*x, x-1, x+1]:
            if 0<=nx<=100000 and graph[nx] == 0:
                graph[nx] = graph[x] +1
                q.append(nx)
                    
n, k = map(int, input().split())
graph=[0]*100001
 
graph[n] = 1
print(bfs(n)-1)
                    

                
            

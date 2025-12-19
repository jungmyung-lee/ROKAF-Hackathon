import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
    
def dfs(x, depth):
    visited[x] = True
    global arrive
    
    if depth == 5:
        arrive = True
        return
    
    for i in graph[x]:
        if not visited[i]:
            dfs(i, depth+1)
    # backtrack so other paths can reuse this node
    visited[x] = False
                    

n,m = map(int, input().split())
                    
visited = [False] * (n)
graph = [[] for i in range(n)]

for i in range(m):
    a,b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

arrive = False
for start_node in range(n):
    dfs(start_node, 1)
    if arrive:
        break
                
if arrive:
    print(1)
else:
    print(0)

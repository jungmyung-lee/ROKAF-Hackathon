import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
    
def dfs(x, depth):
    visited[x] = True
    found = False
    if depth == 5:
        found = True
    else:
        for nxt in graph[x]:
            if not visited[nxt]:
                if dfs(nxt, depth + 1):
                    found = True
                    break
    # backtrack so other paths can reuse this node
    visited[x] = False
    return found
                    

n,m = map(int, input().split())
                    
visited = [False] * n
graph = [[] for _ in range(n)]

for i in range(m):
    a,b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

for start_node in range(n):
    if dfs(start_node, 1):
        print(1)
        sys.exit()
print(0)

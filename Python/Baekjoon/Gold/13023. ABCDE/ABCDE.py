import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, depth):
    visited[x] = True
    if depth == 5:
        visited[x] = False
        return True
    for nxt in graph[x]:
        if not visited[nxt] and dfs(nxt, depth + 1):
            visited[x] = False
            return True
    visited[x] = False
    return False

n, m = map(int, input().split())

visited = [False] * n
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for start_node in range(n):
    if dfs(start_node, 1):
        print(1)
        sys.exit()
print(0)

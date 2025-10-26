import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input()) # 정점의 개수

# 그래프 정보
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, weight = map(int, input().split())  # 부모, 자식, 가중치
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))

# DFS 함수
def DFS(x, distance):
    for i, w in graph[x]:
        # 아직 방문하지 않은 노드이면 현재까지의 거리 + 해당 노드까지의 가중치로 방문 배열 값을 변경
        if visited[i] == -1:
            visited[i] = distance + w
            DFS(i, distance + w)

# 루트 노드에서 각 정점까지의 거리 계산
visited = [-1] * (n+1)
visited[1] = 0  # 루트 노드 거리는 0으로 초기화
DFS(1, 0)
max_distance = max(visited) # 최장 거리
max_node = visited.index(max_distance) # 해당 노드


# max_node에서 시작해 각 정점까지의 거리 계산
visited = [-1] * (n+1)
visited[max_node] = 0 
DFS(max_node, 0)

print(max(visited)) # 최장 거리(=트리의 지름) 출력
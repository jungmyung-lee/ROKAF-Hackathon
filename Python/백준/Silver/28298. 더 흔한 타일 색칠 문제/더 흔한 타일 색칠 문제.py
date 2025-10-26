n,m,k = map(int, input().split())
graph = []
cnt_list = [0] * 26
    
for i in range(n):
    row = list(input())
    graph.append(row)
        
total = 0
k_num = n*m // k**2
        
for x in range(k):
    for y in range(k):
        
        cnt_list = [0] * 26
        for i in range(0, n-k+1,k):
            for j in range(0, m-k+1, k):
                g = graph[i+x][j+y]
                cnt_list[ord(g)-65] += 1
        max_cnt = max(cnt_list)
        total += k_num - max_cnt
        
        for i in range(0, n-k+1,k):
            for j in range(0, m-k+1, k):
                graph[i+x][j+y] = chr(cnt_list.index(max_cnt) +65)
                    
print(total)
for i in range(n):
    print("".join(graph[i]))


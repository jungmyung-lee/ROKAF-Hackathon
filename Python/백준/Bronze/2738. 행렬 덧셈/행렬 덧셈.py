n,m= map(int, input().split())
graph1 = []
graph2 = []
    
for i in range(n):
    row = list(map(int, input().split()))
    graph1.append(row)
        

for i in range(n):
    row = list(map(int, input().split()))
    graph2.append(row)
        
for i in range(n):
    for j in range(m):
        graph1[i][j] += graph2[i][j]
        graph1[i][j] = str(graph1[i][j])
        
for i in range(n):
    print(" ".join(graph1[i]))
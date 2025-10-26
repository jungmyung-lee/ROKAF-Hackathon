n,m = map(int, input().split())

graph=[]
graph2=[[0]*n for i in range(m)]
d={'.':'.','O':'O','-':'|','|':'-','\\':'/','/':'\\','^':'<','<':'v','v':'>','>':'^'}

for i in range(n):
    row=list(input())
    graph.append(row)
    

   
for i in range(n):
    for j in range(m):
        graph2[m-j-1][i] = d[graph[i][j]]
        
for i in range(m):
    print("".join(graph2[i]))
        

       

graph = [[0] * 100 for i in range(100)]

n = int(input())
for i in range(n):    
    a,b= map(int, input().split())
        
    for i in range(a-1,a+9):
        for j in range(b-1,b+9):
            graph[j][i] =1
max = 0           
for i in range(100):
    max += sum(graph[i])
    
print(max)
            
    
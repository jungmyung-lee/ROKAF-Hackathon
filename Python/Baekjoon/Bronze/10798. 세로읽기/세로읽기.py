graph=[]

for i in range(5):
    row= list(input())
    graph.append(row)
        
s = ""
    
for i in range(15):
    for j in range(5):
        if i <= len(graph[j]) -1:
            s+= graph[j][i]
            
print(s)
                
    
        
        
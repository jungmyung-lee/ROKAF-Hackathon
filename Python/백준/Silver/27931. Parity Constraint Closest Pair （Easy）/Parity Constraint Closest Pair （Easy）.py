dis = []
n = int(input())
graph = list(map(int, input().split()))
graph.sort()
dis=[]

for i in range(n-1):
    dis.append(graph[i+1] - graph[i])
    
for i in range(n-2):
    dis.append(graph[i+2] - graph[i])

dis.sort()

find1 = False
find2 = False
n_list = [-1] * 2

for i in dis:
    if i% 2 ==0 and not find1:
        find1= True
        n_list[0] = i
    if i % 2 != 0 and not find2:
        find2 = True
        n_list[1] = i
    if find1 and find2:
        break

    

print(*n_list)
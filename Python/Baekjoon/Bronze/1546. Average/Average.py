N = int(input())
n_list = list( map(int, input().split()) )
max = max(n_list)


for i in range(N):
    n_list[i] = n_list[i] / max * 100
    
print(sum(n_list)/N)

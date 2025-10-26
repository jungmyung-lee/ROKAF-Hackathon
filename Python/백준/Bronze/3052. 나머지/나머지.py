n_list = []

for i in range(10):
    a = int(input())
    n_list.append(a%42)
        
print(len(set(n_list)))
    

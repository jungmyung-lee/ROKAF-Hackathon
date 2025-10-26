T = int(input())
n_list = [25, 10, 5, 1]

for i in range(T):
    total = int(input())
    for j in range(4):
        print(total // n_list[j], end=" ")
        total = total % n_list[j]
    print()
        
        
    
    
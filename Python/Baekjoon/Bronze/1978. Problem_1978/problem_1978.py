n = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in range(n):
    a = A[i]
    
    if a==1:
        continue
        
    
    if a == 2:
        cnt+= 1
        continue
    
    for j in range(2,a):
        if a % j == 0:
            break
    else:
        cnt+=1
            
print(cnt)
            
            
    
        

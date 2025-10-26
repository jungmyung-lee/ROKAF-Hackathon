m = int(input())
n = int(input())
ans = []
    
for i in range(m, n+1):

    if i == 1:
        continue
            
    if i == 2:
        ans.append(i)
        continue
            
            
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        ans.append(i)
            
if not ans:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))
                
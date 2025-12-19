n = int(input())
A = list(map(int, input().split()))
B = A[::-1]
dp1 = [1] * n
dp2 = [1] * n
res = 1
for i in range(1,n):
    for j in range(i):
        if A[i] > A[j] :
            dp1[i] = max(dp1[i], dp1[j] + 1)
        if B[i] > B[j]: 
            dp2[i] = max(dp2[i], dp2[j] + 1)
    
dp2= dp2[::-1]        
for i in range(n):
    res= max(res, dp1[i] + dp2[i])
print(res-1)
    
                
    
    
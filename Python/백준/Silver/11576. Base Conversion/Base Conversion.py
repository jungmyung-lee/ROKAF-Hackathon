a,b = map(int, input().split())
m = int(input())
A = list(map(int, input().split()))
A = A[::-1]
ans = 0
    
for i in range(m):
    ans += A[i]*a**i
s = []   
while ans:
    s.append(ans % b)
    ans //= b
        
s = s[::-1]
print(*s)

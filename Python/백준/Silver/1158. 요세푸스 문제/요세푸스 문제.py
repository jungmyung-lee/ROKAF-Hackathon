N, K = map(int, input().split())
A=[]
answer=[]

for i in range(1, N+1):
    A.append(i)

idx = 0
while A:
    idx = (idx + K -1) % len(A)  
    answer.append(A.pop(idx))
    
s = ", ".join([str(x) for x in answer])
print("<"+s+">")
    

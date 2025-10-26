N, M = map(int, input().split())
A = list(map(int, input().split() ))

max = 3

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            B = [A[i], A[j], A[k]]
            if sum(B) <= M and sum(B) > max :
                max = sum(B)
                
                
print(max)
            
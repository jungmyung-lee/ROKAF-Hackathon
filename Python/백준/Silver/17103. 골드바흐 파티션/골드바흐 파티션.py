K = int(input())
T = [True] * 1000001

for i in range(2, int(1000000**0.5)+1):
    if T[i] :
        for j in range(i*2, 1000001, i):
            T[j] = False  

for i in range(K):
    cnt = 0
    N = int(input())
    for j in range(3, N//2+1, 2):
        if T[j] and T[N-j]:
            cnt += 1
    if T[2] and T[N-2]:
        cnt += 1
            
    print(cnt)
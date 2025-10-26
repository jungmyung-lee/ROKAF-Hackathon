import sys
Q = []

N = int(sys.stdin.readline())

for i in range(N):
    S = sys.stdin.readline().split()
    
    if S[0] == "push":
        Q.append(S[1])
    elif S[0] == "pop":
        if Q:
            print(Q.pop(0))
        else:
            print(-1)
    elif S[0] == "size":
        print(len(Q))
    elif S[0] == "empty":
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    elif S[0] == "front":
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[0])
    elif S[0] == "back":
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[-1])
            
        
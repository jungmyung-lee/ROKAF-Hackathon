import sys

N = int(input())
D = []

for i in range(N):
    S = sys.stdin.readline().split()
    if S[0] == "push_front":
        D.insert(0, S[1])
    elif S[0] == "push_back":
        D.append(S[1])
    elif S[0] == "pop_front":
        if D:
            print(D.pop(0))
        else:
            print(-1)
    elif S[0] == "pop_back":
        if D:
            print(D.pop())
        else:
            print(-1)
    elif S[0] == "size":
        print(len(D))
    elif S[0] == "empty":
        if D:
            print(0)
        else:
            print(1)
    elif S[0] == "front":
        if D:
            print(D[0])
        else:
            print(-1)
    elif S[0] == "back":
        if D:
            print(D[-1])
        else:
            print(-1)
    
    
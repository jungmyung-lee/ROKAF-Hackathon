import sys

N = int(sys.stdin.readline())
A = []

for i in range(N):
    S = sys.stdin.readline().strip()
    
    s = S.split()
    if s[0] == "push":
        A.append(int(s[-1]))
    elif S == "pop":
        if len(A) ==0:
            print(-1)
        else:
            print(A.pop())
    elif S == "size":
        print(len(A))
    elif S == "empty":
        if len(A) == 0:
            print(1)
        else:
            print(0)
    elif S == "top":
        if (len(A) ==0):
            print(-1)
        else:
            print(A[-1])
        
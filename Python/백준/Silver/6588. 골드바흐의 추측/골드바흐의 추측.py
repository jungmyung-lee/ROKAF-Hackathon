import sys
input = sys.stdin.readline

A= [True] * 1000001
for i in range(2, int(1000001**0.5) + 1):
    if A[i]:
        for j in range(2*i, 1000001, i):
            A[j] = False

while True:
    n = int(input())
    if n ==0:
        break
     
    for i in range(3, n//2+1, 2):
        if A[i] and A[n-i]:
            print(n, "=", " + ".join([ str(i), str(n-i) ]))
            break
    else:
        print("Goldbach's conjecture is wrong.")
    
    
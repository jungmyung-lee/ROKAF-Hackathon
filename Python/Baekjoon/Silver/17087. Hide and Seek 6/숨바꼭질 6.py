from functools import reduce
import math

n,s = map(int, input().split())
A = list(map(int, input().split()))
B= []

for i in range(0, n):
    B.append(abs(s- A[i]))
    
result = reduce(math.gcd, B)

print(result)
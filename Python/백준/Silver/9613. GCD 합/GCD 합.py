from collections import deque
import math
import sys



n = int(sys.stdin.readline())


for i in range(n):
    stack = deque(list(map(int, sys.stdin.readline().split())))
    total = []
    k = stack.popleft()
    for a in range(k-1):
        for b in range(a+1, k):
            total.append(math.gcd(stack[a], stack[b]))
    print(sum(total))
                  
    
                  
        




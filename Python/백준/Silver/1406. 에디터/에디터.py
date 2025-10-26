import sys

left = list(input())
n =int(sys.stdin.readline())

right = []

for i in range(n):
    Snew = list(sys.stdin.readline().split())
    if Snew[0] == "L" and left:
        right.append(left.pop())
    elif Snew[0] == "D" and right:
        left.append(right.pop())
    elif Snew[0] == "B" and left:
        left.pop()
    elif Snew[0] == "P":
        left.append(Snew[1])
        
        
answer = left + right[::-1]
print("".join(answer))


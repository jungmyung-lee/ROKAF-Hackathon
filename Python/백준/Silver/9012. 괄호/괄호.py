n = int(input())
    
for i in range(n):
    stack = []
    S= input()
    for i in S:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")
    
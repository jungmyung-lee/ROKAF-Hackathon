from collections import deque

S = input()
stack = deque([])
check = False
ans = ""

for i in S:
    if i == "<":
        check = True
        while stack:
            ans += stack.pop()
            
    stack.append(i)
    
    if i== ">":
        check = False
        while stack:
            ans+= stack.popleft()
    
    if i==" " and check==False:
        stack.pop()
        while stack:
            ans+= stack.pop()
        ans += " "
        
if stack:
    while stack:
        ans += stack.pop()

print(ans)
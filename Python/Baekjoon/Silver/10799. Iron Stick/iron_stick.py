S = input()
cnt =0
stack= []

for i in range(len(S)):
    if S[i] == "(":
        stack.append("(")
    else:
        stack.pop()
        if S[i-1] == "(":
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)
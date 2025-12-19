word = []
meaning = []

n,m = map(int, input().split())

for i in range(n):
    P = list(input().split())
    word.append(P[0])
    meaning.append(P[1])
    #print(word)
    #print(meaning)
    
for i in range(m):
    S = input()
    ans = ""
    
    for i in range(len(S)):
        text=""
        
        for j in range(i, len(S)):
            text += S[j]
    
            if text in word:
                ans += meaning[word.index(text)]
                #print(ans)
    if ans != "":            
        print(ans)
    else:
        print(-1)
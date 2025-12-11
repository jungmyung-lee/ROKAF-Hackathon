n,q = map(int, input().split())
S = list(input())
for i in range(q):
    a,b,c = map(int, input().split())
    idx1 = b-1
    idx2 = c-1
    cnt = 1
   
    
    if a == 1:
        for i in range(idx1, idx2):
            if S[i] == S[i+1] :
                continue
            else:
                cnt += 1
        print(cnt)
        

    if a == 2:
        idx1 = b-1
        idx2 = c-1
        
        
        for i in range(idx1, idx2 +1):
            if ord(S[i]) == 90:
                S[i] = 'A'
            else:
                S[i] = chr(ord(S[i]) + 1)
        
    

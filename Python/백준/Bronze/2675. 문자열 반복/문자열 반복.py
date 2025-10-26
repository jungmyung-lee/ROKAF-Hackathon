n = int(input())
    
for i in range(n):
    k,s = input().split()
    k = int(k)
       
    res = ""
    for j in s:
        res += j*k
        
    print(res)
    
    
S = input()
    
A = ["ABC","DEF","GHI","JKL","MNO", "PQRS", "TUV", "WXYZ"]
   
res = 0
for j in S:
    for i in A:
        if j in i:
            res += A.index(i) +3
            break
            
            
     
print(res)
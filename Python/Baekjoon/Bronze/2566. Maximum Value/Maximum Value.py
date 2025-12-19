A = []
r = 0
c = 0

for i in range(9):
    row = list(map(int, input().split() ))
    A.append(row)
    
max = A[0][0]
    
for i in range(9):
    for j in range(9):
        if A[i][j] >= max:
            max = A[i][j]
            r = i+1
            c = j+1
            
print(max)
print(r, c)
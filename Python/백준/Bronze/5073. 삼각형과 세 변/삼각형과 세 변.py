while True:
    A = list(map(int, input().split() ))
    if sum(A) ==0:
        break
        
    if max(A) >= sum(A) - max(A):
        print("Invalid")
    
    elif len(set(A)) == 1:
        print("Equilateral")
        
    elif len(set(A)) == 2:
        print("Isosceles")
        
    elif len(set(A)) == 3:
        print("Scalene")
A = [int(input()) for i in range(3)]

if A.count(60) == 3:
    print("Equilateral")
    
elif sum(A) == 180 and len(set(A)) ==2:
    print("Isosceles")
    
elif sum(A) == 180 and len(set(A)) == 3:
    print("Scalene")
    
elif (sum(A) != 180):
    print("Error")

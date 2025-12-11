A = list(map(int, input().split() ))



if ( max(A) < sum(A) - max(A) ):
    print(sum(A))
    
else:
    max1 = sum(A) - max(A) -1
    print(max1 + sum(A) -max(A))
    


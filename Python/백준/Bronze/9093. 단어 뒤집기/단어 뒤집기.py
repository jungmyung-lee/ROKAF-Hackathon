n=int(input())

for i in range(n):
    A = input().split()
    A = [x[::-1] for x in A]
    
    for word in A:
        print(word, end=" ")
n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in range(m):
    a.sort()
    b= a[0]+a[1]
    a[0]=b
    a[1]=b 
print(sum(a))
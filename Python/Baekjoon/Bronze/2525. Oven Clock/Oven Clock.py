H, M = map(int, input().split())
timer = int(input())

H = H + (timer // 60)
M = M + (timer % 60)

if (M >= 60): 
    H = H + 1
    M = M -60
if (H >= 24):
    H = H -24
print(H,M)





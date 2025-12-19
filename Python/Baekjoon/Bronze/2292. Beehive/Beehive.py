N = int(input())
cnt = 1
piles_num = 1

while N > piles_num:
    piles_num += 6 * cnt
    cnt += 1
    
print(cnt)
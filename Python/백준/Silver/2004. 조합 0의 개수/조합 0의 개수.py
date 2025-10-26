n,m = map(int, input().split())

def two_cnt(x):
    two = 0
    while x != 0:
        x //= 2
        two += x
    return two 

def five_cnt(x):
    five = 0
    while x != 0:
        x //= 5
        five += x
    return five

print(min(two_cnt(n) -two_cnt(m) - two_cnt(n-m), five_cnt(n) - five_cnt(m) - five_cnt(n-m)))
    
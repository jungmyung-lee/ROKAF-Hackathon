N = int(input())
n_list = list(map(int, input().split() ))
max = n_list[0]
min = n_list[0]


for i in n_list[1:]:
    if max < i: max = i
    if min > i: min = i

print(min, max)
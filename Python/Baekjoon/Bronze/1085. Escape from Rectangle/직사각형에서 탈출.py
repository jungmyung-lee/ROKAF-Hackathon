x,y,w,h = map(int, input().split())

n_list= [x, y, w-x, h-y]

print(min(n_list))
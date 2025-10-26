x_nums=[]
y_nums=[]

for i in range(3):
    A,B = map(int, input().split())
    x_nums.append(A)
    y_nums.append(B)
    
for i in range(3):
    if x_nums.count(x_nums[i]) == 1:
        x = x_nums[i]
    if y_nums.count(y_nums[i]) == 1:
        y = y_nums[i]
        
print(x, y)
    
    
    
    
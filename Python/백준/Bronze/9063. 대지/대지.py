N = int(input())

x_nums = []
y_nums= []

    

for i in range (N):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)
        
a = max(x_nums) - min(x_nums)
b = max(y_nums) - min(y_nums)
    
print(a * b)
        
        
        
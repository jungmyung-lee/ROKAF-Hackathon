n = int(input())
s =""
if n ==0:
    print(0)
    exit()

while n!= 0:
    if n % -2 == 0:
        n //= -2
        s+= "0"
    else:
        n = n//-2 +1
        s+= "1"
            
print(s[::-1])
    
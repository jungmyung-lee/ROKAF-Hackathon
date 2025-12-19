x = input()

def checknum(n):
    length = len(n)
    A_list = [n[0], n[:2], n[:3]]
    for A in A_list:
        res = ""
        B = int(A)
        while len(res) < length:
            res += str(B)
            
            if res == n:
                return A,B
            
            B += 1
    return n,n
            
print(*checknum(x))
while True:
    ans = []
    s = int(input())
    if s == -1:
        break
    for i in range(1, s):
        if s % i == 0:
            ans.append(i)
                
    if sum(ans) == s:
    
        print(str(s) +" = " + " + ".join(map(str,ans)))
    else:
        print(str(s) +" is NOT perfect.")
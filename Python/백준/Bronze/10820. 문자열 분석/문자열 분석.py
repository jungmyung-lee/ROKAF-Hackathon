    
    
while True:
    upper = 0
    lower =0
    blank = 0
    num = 0
    
    try:
        S = input()
        for j in range(len(S)):
            if 65<= ord(S[j]) <= 90:
                upper += 1
            elif 97<= ord(S[j]) <= 122:
                lower += 1
            elif S[j] == " ":
                blank += 1
            else:
                num += 1
    except:
        break
    print(lower, upper, num, blank)
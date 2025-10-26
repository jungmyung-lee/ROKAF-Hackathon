s = input()

flag = 0
cnt = 0
ucpc = "UCPC"
for i in s:
    if i == ucpc[cnt]:
        cnt+=1
    if cnt == 4:
        print("I love UCPC")
        flag = 1
        break
if flag == 0:
    print("I hate UCPC")
    
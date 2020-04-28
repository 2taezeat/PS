t = int(input())

for i in range(t):
    s = input()
    sum1 = 0
    ocount = 0
    for c in s:
        
        if c == 'O':
            sum1 = sum1 + 1 + ocount
            ocount = ocount + 1
        else:
            ocount = 0


    print(sum1)
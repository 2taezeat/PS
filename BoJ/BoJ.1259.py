while(True):
    s = input()
    p = 0
    if s == '0':
        break

    else:
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                p = 1

    if p ==0:
        print('yes')
    elif p == 1:
        print('no')
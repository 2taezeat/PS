while(True):
    a, b, c = map(int,input().split())
    l = []
    if a == 0 and b == 0 and c == 0:
        break
    else:
        l.append(a)
        l.append(b)
        l.append(c)
        l.sort()

        if l[0]**2 + l[1]**2 == l[2]**2:
            print('right')
        else:
            print('wrong')

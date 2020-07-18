t = int(input())

for i in range(t):
    pl = list(input())
    if pl[-1] == '(':
        print('NO')
        continue
    if pl[0] == ')':
        print('NO')
        continue
    if (len(pl) % 2) == 1:
        print('NO')
        continue

    l,r,u = 0,0,0

    for p in pl:
        if p == '(':
            l = l + 1
 
        elif p == ')':
            r = r + 1
   
        if l < r:
            print('NO')
            u = 1
            break
        
    if u == 0:
        
        if l != r:
            print('NO')
        elif l == r:
            print('YES')
    
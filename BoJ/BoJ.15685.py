N = int(input())
finput = []
entirespace = []
for i in range(N):
    a = list(map(int,input().split()))
    finput.append(a)

for l in finput:
    space = [[ l[0],l[1] ]]
    dlist = [ l[2] ]
    gen = l[3]
    if dlist[0] == 0:
        nx, ny = space[-1][0] + 1 ,space[-1][1]
    if dlist[0] == 1:
        nx, ny = space[-1][0] ,space[-1][1] - 1
    if dlist[0] == 2:
        nx, ny = space[-1][0] - 1 ,space[-1][1]
    if dlist[0] == 3:
        nx, ny = space[-1][0], space[-1][1] + 1
    space.append( [nx,ny] )

    for g in range(1,gen+1):
        ld = len(dlist)
        for j in range(ld):
            h = ld-j-1
            d = dlist[h] + 1
            if d == 4:
                d = 0

            if d == 0:
                nx, ny = space[-1][0] + 1 ,space[-1][1]
            if d == 1:
                nx, ny = space[-1][0] ,space[-1][1] - 1
            if d == 2:
                nx, ny = space[-1][0] - 1 ,space[-1][1]
            if d == 3:
                nx, ny = space[-1][0], space[-1][1] + 1

            space.append( [nx,ny] )
            dlist.append(d)
    entirespace = entirespace + space

count = 0
entirespace = list(set(map(tuple, entirespace)))
for a in entirespace:
    x = a[0]
    y = a[1]
    if (x+1, y+1) in entirespace and (x, y+1) in entirespace and (x+1, y) in entirespace:
        count = count + 1

print(count)
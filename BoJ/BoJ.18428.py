import sys,copy
from itertools import combinations
from collections import deque
n = int(input())
space = []
for i in range(n):
    space.append(list(input().split()))
tl,sl,xl = [],[],[]
for i in range(n):
    for j in range(n):
        if space[i][j] == 'T':
            tl.append([i,j])
        if space[i][j] == 'S':
            sl.append([i,j])
        else:
            xl.append([i,j])

cb = list(combinations(xl,3))

for c in cb:
    nsp = copy.deepcopy(space)
    q,w,e = c[0],c[1],c[2]
    x1,y1 = q[0],q[1]
    x2,y2 = w[0],w[1]
    x3,y3 = e[0],e[1]
    nsp[x1][y1] = 'O'
    nsp[x2][y2] = 'O'
    nsp[x3][y3] = 'O'
    check = 0


    for te in tl:
        tx = te[0]
        ty = te[1]
        
        for i in range(4):
            tx = tx + 1
            ty = ty
            
            if 0 <= tx < n and 0 <= ty < n:
                if nsp[tx][ty] == "O":
                    break
                if nsp[tx][ty] == "S":
                    check = 1
                    break

        tx = te[0]
        ty = te[1]

        for i in range(4):
            tx = tx - 1
            ty = ty
            
            if 0 <= tx < n and 0 <= ty < n:
                if nsp[tx][ty] == "O":
                    break
                if nsp[tx][ty] == "S":
                    check = 1
                    break

        tx = te[0]
        ty = te[1]

        for i in range(4):
            tx = tx
            ty = ty + 1
            
            if 0 <= tx < n and 0 <= ty < n:
                if nsp[tx][ty] == "O":
                    break
                if nsp[tx][ty] == "S":
                    check = 1
                    break

        tx = te[0]
        ty = te[1]

        for i in range(4):
            tx = tx
            ty = ty - 1
            
            if 0 <= tx < n and 0 <= ty < n:
                if nsp[tx][ty] == "O":
                    break
                if nsp[tx][ty] == "S":
                    check = 1
                    break


    if check == 0:
        print("YES")
        exit()

print("NO")
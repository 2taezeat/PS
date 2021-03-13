import sys, collections
R, C, T = map(int,sys.stdin.readline().split())
space = []
cleaner = []
xl = [0,1,0,-1]
yl = [-1,0,1,0]
for i in range(R):
    l = list(map(int,sys.stdin.readline().split()))
    space.append(l)
    if l[0] == -1:
        cleaner.append(i)

time, answer = 0, 0
while(time < T):
    # 1단계
    q = collections.deque()
    l1 = []
    for i in range(R):
        for j in range(C):
            if space[i][j] > 0 :
                q.append([i,j])

    while (q):
        I, J = q.popleft()
        c = 0
        for k in range(4):
            dx = J + xl[k]
            dy = I + yl[k]

            if 0 <= dx < C and 0<= dy < R and space[dy][dx] != -1:
                c = c + 1
                v = space[I][J] // 5
                l1.append([dx, dy, v, c])

        space[I][J] = space[I][J] - (v)*c

    for info in l1:
        space[ info[1] ] [ info[0] ] = space[ info[1] ] [ info[0] ] + info[2] 
 
    ## 2단계
    l2 = []

    for i in range(0, cleaner[0]):
        l2.append( [i, 0, space[i][0], 4 ] )
    for i in range(cleaner[1],R-1):
        l2.append( [i, C-1, space[i][C-1], 4 ] )

    for i in range(1,cleaner[0]+1):
        l2.append( [i, C-1, space[i][C-1], 3 ] )
    for i in range(cleaner[1]+1, R):
        l2.append( [i, 0, space[i][0], 3 ] )

    for j in range(1,C):
        l2.append( [0, j, space[0][j], 2 ] )
    for j in range(1,C):
        l2.append( [R-1, j, space[R-1][j], 2 ] )

    for j in range(1,C-1):
        l2.append( [cleaner[0], j, space[cleaner[0]][j], 1 ] )
    for j in range(1,C-1):
        l2.append( [cleaner[1], j, space[cleaner[1]][j], 1 ] )


    for p in l2:
        if p[3] == 1:
            space[ p[0] ][ p[1]+1 ] = p[2] 
        if p[3] == 2:
            space[ p[0] ][ p[1]-1 ] = p[2] 
        if p[3] == 3:
            space[ p[0]-1 ][ p[1] ] = p[2] 
        if p[3] == 4:
            space[ p[0]+1 ][ p[1] ] = p[2]

    space[ cleaner[0] ][1] = 0
    space[ cleaner[1] ][1] = 0
    space[ cleaner[0] ][0] = -1
    space[ cleaner[1] ][0] = -1

    time = time + 1

for i in range(R):
    for j in range(C):
        answer = answer + space[i][j]

print(answer+2)
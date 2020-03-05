import sys
M, N = map(int,input().split())
space = []
s,r  = 1, 1
ol,q = [], []
for i in range(N):
    l1 = list(map(int,input().split()))
    if 0 in l1:
        s = 50
    space.append(l1)

dx = [0, 1 , 0 ,-1 ] #위, 오른쪽, 아래, 왼쪽
dy = [-1, 0, 1,  0]

if s != 50:
    print(0)
else:
    for i in range(N):
        for j in range(M):
            if space[i][j] == 1:
                ol.append([i,j])

    for a in ol:
        y = a[0]
        x = a[1]
        q.append([y,x])

    next1 = []
    while q:
        now = q.pop()

        for i in range(4):
            nowx = now[1] + dx[i]
            nowy = now[0] + dy[i]

            if 0 <= nowx < M and 0 <= nowy < N and space[nowy][nowx] == 0:
                space[nowy][nowx] = r
                next1.append( [nowy,nowx] )

        if q == []:
            q = q + next1
            r = r + 1
            next1 = []

    for i in range(N):
        l1 = space[i]
        if 0 in space[i]:
            s = -1
            break

    if s == -1:
        print(s)
    else:
        print(r-2)
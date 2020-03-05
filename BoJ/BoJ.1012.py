import sys
def bfs(y,x,space,rc):
    q = [ [y,x] ]

    while ( q != [] ):
        now = q.pop(0)

        for i in range(4):
            nowx = now[1] + dx[i]
            nowy = now[0] + dy[i]

            if 0 <= nowx < M and 0<= nowy < N and space[nowy][nowx] == 1:
                space[nowy][nowx] = rc
                q.append( [nowy,nowx] )

T = int(input())
dx = [0, 1 , 0 ,-1 ] #위, 오른쪽, 아래, 왼쪽
dy = [-1, 0, 1,  0]
for i in range(T):
    M ,N, K = map(int,input().split())
    space = [ [0] * M for i in range(N)]
    for j in range(K):
        x, y = map(int,input().split())
        space[y][x] = 1

    color = 1000
    rcl = []

    for i in range(N):
        for j in range(M):
            color = color + 1

            if space[i][j] == 1:
                rc = color
                space[i][j] = rc
                bfs(i,j,space,rc)
                rcl.append(rc)
    
    print(len(rcl))

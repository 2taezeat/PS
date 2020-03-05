import sys

N = int(input())
space = [ [3] * N for i in range(N)]
for i in range(N):
    l1 = list(map(int,input()))
    space[i] = l1

dx = [0, 1 , 0 ,-1 ] #위, 오른쪽, 아래, 왼쪽
dy = [-1, 0, 1,  0]

def bfs(y,x):
    global space
    global rc
    global result 
    q = [ [y,x] ]

    while ( q != [] ):
        now = q.pop(0)

        for i in range(4):
            nowx = now[1] + dx[i]
            nowy = now[0] + dy[i]

            if 0 <= nowx < N and 0<= nowy < N and space[nowy][nowx] == 1:
                space[nowy][nowx] = rc
                q.append( [nowy,nowx] )
                result.append(rc) 


color = 1000
rcl = []
result = []
for i in range(N):
    for j in range(N):
        color = color + 1

        if space[i][j] == 1:
            rc = color
            result.append(rc)
            space[i][j] = rc
            bfs(i,j)
            rcl.append(rc)

print(len(rcl))
a = []
for r in rcl:
    b = 0
    for i in result:
        if r == i:
            b = b + 1

    a.append(b)

a.sort()
for i in a:
    print(i)
import copy
N = int(input())
space = [list(map(int,input().split())) for i in range(N)]
m = max(max(space))
dx = [0, 1 , 0 ,-1 ] #위, 오른쪽, 아래, 왼쪽
dy = [-1, 0, 1,  0]

def bfs(y,x,nspace):
    q = [ [y,x] ]
    r = []
    while ( q != [] ):
        now = q.pop(0)
        for i in range(4):
            nowx = now[1] + dx[i]
            nowy = now[0] + dy[i]

            if 0 <= nowx < N and 0<= nowy < N and nspace[nowy][nowx] >= 0:
                nspace[nowy][nowx] = -2
                q.append( [nowy,nowx] )
    
answer = []
for i in range(0,m+1):
    nspace = copy.deepcopy(space)
    a = 0
    for y in range(N):
        for x in range(N):
            if nspace[y][x] <= i:
                nspace[y][x] = -1

    for y in range(N):
        for x in range(N):
            if nspace[y][x] >= 0:
                a = a + 1
                bfs(y,x,nspace)
    
    answer.append(a)

print(max(answer))
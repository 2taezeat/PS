import itertools
import copy
N , M = map( int, input().split() )
ospace, ol, cl, result  = [], [], [], []

for i in range(N):
    ospace.append(list(map(int,input().split())))
dx = [0, 1 , 0 ,-1 ] #위, 오른쪽, 아래, 왼쪽
dy = [-1, 0, 1,  0]
for i in range(N):
    for j in range(M):
        if ospace[i][j] == 0:
            cl.append([i,j])

        if ospace[i][j] == 2:
            ol.append([i,j])

c = list (map( tuple, itertools.combinations(cl, 3) ) )

def bfs(y,x,newspace):
    q = [[y,x]]

    while q:
        now = q.pop()
        
        for i in range(4):
            nowx = now[1] + dx[i]
            nowy = now[0] + dy[i]

            if 0 <= nowx < M and 0 <= nowy < N and newspace[nowy][nowx] == 0:
                newspace[nowy][nowx] = 2
                q.append([nowy,nowx])

for wall in c:
    i0, j0, i1, j1, i2, j2 = *wall[0], *wall[1], *wall[2]
    newspace = copy.deepcopy(ospace)
    newspace[i0][j0] = 1
    newspace[i1][j1] = 1
    newspace[i2][j2] = 1

    for o in ol:
        bfs(*o,newspace)

    count = 0
    for i in range(N):
        for j in range(M):
            if newspace[i][j] == 0:
                count = count + 1

    result.append(count)

print(max(result))
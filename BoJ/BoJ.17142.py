import itertools, collections
N, M = map(int,input().split())
space = []
result = 999999999
dy = [0,0,1,-1]
dx = [-1,1,0,0]
bias_loaction = []
blankcount = 0
for i in range(N):
    aa = list(map(int,input().split()))
    for a in range(len(aa)):
        if aa[a] == 2:
            bias_loaction.append((i,a))
        elif aa[a] == 0:
            blankcount +=1
    space.append(aa)

comb = list ( itertools.combinations(bias_loaction,M) )
if blankcount == 0:
    print(0)
    exit()

for cc in comb:
    visit = [[0 for a in range(N)] for b in range(N)]
    q = collections.deque()
    bc = 0
    for (i,j) in cc:
        q.append((i,j))
        visit[i][j] = 100

    # bfs
    while (q):
        y,x  = q.popleft()
        value = 0
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<= ny <N and 0<= nx <N and space[ny][nx] != 1 and visit[ny][nx] == 0:
                visit[ny][nx] = visit[y][x] + 1   
                q.append((ny,nx))
                value = visit[ny][nx]
                if space[ny][nx] == 0:
                    bc +=1

        if value > result:
            break

        if bc == blankcount:
            result = min(result,value)
            break

if result == 999999999:
    print(-1)
else:
    print(result - 100 )
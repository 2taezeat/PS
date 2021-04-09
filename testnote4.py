import itertools, copy, collections
N, M = map(int,input().split())
space = []
result = []
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
def finish_check(n_space):
    for i in range(N):
        for j in range(N):
            if n_space[i][j] == 0:
                return False
    return True

if blankcount == 0:
    print(0)
    exit()

for cc in comb:
    n_space = copy.deepcopy(space)
    q = collections.deque()
    for (i,j) in cc:
        n_space[i][j] = 1000 # 활성 
        q.append((i,j))
    
    bc = 0
    # bfs
    while (q):
        #print(q)
        # if finish_check(n_space) == True:
        #     result.append(max(map(max, n_space)))
        #     break
    
        y,x  = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<= ny <N and 0<= nx <N and n_space[ny][nx] != 1 and ( n_space[ny][nx] == 0 or n_space[ny][nx] == 2 ):
                if n_space[ny][nx] == 2:
                    n_space[ny][nx] = n_space[y][x] + 1
                    q.append((ny,nx))
                else:
                    n_space[ny][nx] = n_space[y][x] + 1
                    q.append((ny,nx))
                    bc +=1

        if bc == blankcount:
            result.append(max(map(max, n_space)))
            break


    # for i in range(N):
    #     print(n_space[i])
    
    # print('------------')

    # print(bc)
                
    
    #result.append(max(map(max, n_space)))
    # if finish_check(n_space) == True:
    #     result.append(max(map(max, n_space)))


if result == []:
    print(-1)
else:
    print(min(result) - 1000 )
import collections, itertools
N,M = map(int,input().split())
space,result = [],[]
for i in range(N):
    space.append(list(map(int,input().split())))
dy = [-1,1,0,0]
dx = [0,0,-1,1]
count = 2
def bfs(b,a, c):
    global space
    q = collections.deque()
    q.append((b,a))
    while(q):
        y,x = q.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= ny < N and 0<= nx < M and space[ny][nx] == 1:
                space[ny][nx] = c
                q.append((ny,nx))

for i in range(N):
    for j in range(M):
        if space[i][j] == 1 :
            space[i][j] = count
            bfs(i,j,count)
            count = count + 1

dhlrkr = []
for i in range(N):
    for j in range(M):
        if space[i][j] > 1:
            if ( 0<= j-1 < M and space[i][j-1] == 0 ) :
                dhlrkr.append(( 4, space[i][j], i,j))

            elif (0<= j+1 < M and space[i][j+1] == 0) :
                dhlrkr.append(( 3, space[i][j], i,j))

            elif (0<= i+1 < N and space[i+1][j] == 0) :
                dhlrkr.append(( 2, space[i][j], i,j))

            elif (0<= i-1 < N and space[i-1][j] == 0 ) :
                dhlrkr.append(( 1, space[i][j], i,j))
            
gnqh = []
def bridging(d,isld, y,x):
    global space
    lth = 0
    if d == 1:
        for i in range(y-1,-1,-1):
            k = space[i][x]
            if k == 0:
                lth += 1
            else:
                return (isld, k, lth)
    elif d == 2:
        for i in range(y+1,N,+1):
            k = space[i][x] 
            if k == 0:
                lth += 1
            else:
                return (isld, k, lth)
    elif d == 3:
        for j in range(x+1,M,+1):
            k = space[y][j] 
            if k == 0:
                lth += 1
            else:
                return (isld, k, lth)
    elif d == 4:
        for j in range(x-1,-1,-1):
            k = space[y][j] 
            if k == 0:
                lth += 1
            else:
                return (isld, k, lth)

for (dire, island, Y,X) in dhlrkr:
    g = bridging(dire, island, Y,X)
    if g:
        gnqh.append(g)
final_list = []
for (i1,i2,leth) in gnqh:
    if leth > 1:
        if (i2,i1,leth) not in final_list:
            final_list.append((i1,i2,leth))
comb = []
for i in range(1,count-2+1):
    comb.append ( list ( itertools.combinations(final_list,i)) )

def link_check(ll):
    r = []
    al = []
    for l in ll:
        if len(l) > 1:
            r.append(l[0])
            al.append(l[0])
            break

    while(r):
        alpha = r.pop()
        for i in ll[alpha]:
            if i not in al:
                al.append(i)
                r.append(i)
    al.sort()
    return al

for i in range(N):
    print(space[i])
ori =  [ i for i in range(0,count-2) ]
#print(ori)
for ccc in comb:
    for cc in ccc:
        island_kind = [ [i] for i in range(0,count-2) ]
        sum1 = 0
        for c in cc:
            a0 = c[0] - 2
            a1 = c[1] - 2
            island_kind[a0].append(a1)
            island_kind[a1].append(a0)
            sum1 = sum1 + c[2]
        

        if link_check(island_kind) == ori:
            #print(cc)
            result.append(sum1)


#print(result)
if result == []:
    print(-1)
else:
    print(min(result))
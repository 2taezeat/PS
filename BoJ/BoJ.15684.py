import itertools,sys # copy는 시간 복잡도가 N 이므로, 시간을 많이씀.
input = sys.stdin.readline
N,M,H = map(int,input().split())
space = [[0]*N for i in range(H)]
h_list = []
for i in range(M):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    space[a][b] = 1
    space[a][b+1] = 2
for i in range(H):
    h = []
    for j in range(N-1):
        if j == 0:
            if space[i][j] == 0 and space[i][1] == 0:
                h.append((0,1,i))
        elif j == N-2:
            if space[i][j] == 0 and space[i][j+1] == 0:
                h.append((j,j+1,i))
        else:
            if space[i][j] == 0 and space[i][j+1] == 0 :
                h.append((j,j+1,i))
    
    h_list.append(h)

def fall(space, frist_x):
    x = frist_x
    for i in range(H):
        if space[i][x] == 1:
            x = x + 1
        elif space[i][x] == 2 :
            x = x - 1

    if x == frist_x:
        return True
    else:
        return False

################### 0시작
q0 = 0
for i in range(N):
    if fall(space,i) == False:
        q0 = 1
        break

if q0 == 0:
    print(0)
    exit()
##################### 1단계
list_1 = []
list_2 = []
list_3 = []
for h in h_list:
    for a,b,c in h:
        list_1.append((a,b,c))

for a,b,c in list_1:
    space[c][a] = 1
    space[c][b] = 2
    q1 = 0
    for i in range(N):
        if fall(space,i) == False:
            space[c][a] = 0
            space[c][b] = 0
            q1 = 1
            break
    
    if q1 == 0:
        print(1)
        exit()
##################### 2단계
aa = list(itertools.combinations(list_1,2))
for a in aa:
    if (a[0][2] == a[1][2] and a[0][1] != a[1][0]) or (a[0][2] != a[1][2]) :
        list_2.append(a)

for l2 in list_2:
    q2 = 0
    y2 = []
    for a,b,c in l2:
        space[c][a] = 1
        space[c][b] = 2
        y2.append((a,b,c))

    for i in range(N):
        if fall(space,i) == False:
            space[y2[0][2]][y2[0][0]] = 0
            space[y2[0][2]][y2[0][1]] = 0

            space[y2[1][2]][y2[1][0]] = 0
            space[y2[1][2]][y2[1][1]] = 0
            q2 = 1
            break
    
    if q2 == 0:
        print(2)
        exit()
##################### 3단계
bb = list(itertools.combinations(list_1,3))

for b in bb:
    if (b[0][2] == b[1][2] and b[0][1] != b[1][0]) or (b[0][2] != b[1][2]) and (b[0][2] == b[2][2] and b[0][1] != b[2][0]) or (b[0][2] != b[2][2]) and (b[1][2] == b[2][2] and b[1][1] != b[2][0]) or (b[1][2] != b[2][2]):
        list_3.append(b)

for l3 in list_3:
    q3 = 0
    y3 = []
    for a,b,c in l3:
        space[c][a] = 1
        space[c][b] = 2
        y3.append((a,b,c))

    for i in range(N):
        if fall(space,i) == False:
            space[y3[0][2]][y3[0][0]] = 0
            space[y3[0][2]][y3[0][1]] = 0

            space[y3[1][2]][y3[1][0]] = 0
            space[y3[1][2]][y3[1][1]] = 0

            space[y3[2][2]][y3[2][0]] = 0
            space[y3[2][2]][y3[2][1]] = 0
            q3 = 1
            break
    
    if q3 == 0:
        print(3)
        exit()

print(-1)
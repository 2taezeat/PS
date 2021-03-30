import itertools, copy
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
    global result_list
    x = frist_x
    for i in range(H):
        if space[i][x] == 1:
            x = x + 1
        elif space[i][x] == 2 :
            x = x - 1

    if x == frist_x:
        #result_list.append(x)
        return True
    else:
        #result_list.append(x)
        return False
# for i in range(N):
#     print(space[i])
################### 0시작
result_list = []
q0 = 0
for i in range(N):
    if fall(space,i) == False:
        q0 = 1
        break

if q0 == 0:
    print(0)
    exit()
##################### 1단계
q1,q2,q3 = 0,0,0
list_1 = []
list_2 = []
list_3 = []
for h in h_list:
    for a,b,c in h:
        list_1.append((a,b,c))

for a,b,c in list_1:
    n_space = copy.deepcopy(space)
    n_space[c][a] = 1
    n_space[c][b] = 2
    q1 = 0
    for i in range(N):
        if fall(n_space,i) == False:
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
    n_space = copy.deepcopy(space)
    q2 = 0
    for a,b,c in l2:
        n_space[c][a] = 1
        n_space[c][b] = 2

    for i in range(N):
        if fall(n_space,i) == False:
            q2 = 1
            break
    
    if q2 == 0:
        print(2)
        exit()
##################### 3단계
bb = list(itertools.combinations(list_1,3))

for b in bb:
    if (b[0][2] == b[1][2] and b[0][1] != b[1][0]) or (b[0][2] != b[1][2]) :
        if (b[0][2] == b[2][2] and b[0][1] != b[2][0]) or (b[0][2] != b[2][2]) :
                if (b[1][2] == b[2][2] and b[1][1] != b[2][0]) or (b[1][2] != b[2][2]):
                    list_3.append(b)

for l3 in list_3:
    n_space = copy.deepcopy(space)
    q3 = 0
    for a,b,c in l3:
        n_space[c][a] = 1
        n_space[c][b] = 2

    for i in range(N):
        if fall(n_space,i) == False:
            q3 = 1
            break
    
    if q3 == 0:
        print(3)
        exit()


print(-1)
import itertools,copy
n , m = map( int, input().split() )
data = [] #초기 맵 리스트
for i in range(n):
    data.append(list(map(int,input().split())))

dx = [0, 1, 0, -1] #위, 오른쪽, 아래, 왼쪽
dy = [-1, 0, 1, 0]
result = 0

# dfs를 이용해 각 바이러스가 사방으로 퍼지도록 하기 함수.
def virus(y,x):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx > -1 and nx < m and ny > -1 and ny < n:
            if temp[ny][nx] == 0:

                temp[ny][nx] = 2
                virus(ny,nx)

##############################################

# 현재 맵에서 안전 영역의 크기를 계산하는 함수.
def safy_space():
    score = 0
    for i in range(n):
        for j in range(m):

            if temp[i][j] == 0:
                score = score + 1
    
    return score
#############################################
cl,l1 = [],[]
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            cl.append([i,j])

comb = list (map( tuple, itertools.combinations(cl, 3) ) )

for c in comb:
    temp = [[0]* m for _ in range(n)]
    i0, j0 = c[0]
    i1, j1 = c[1]
    i2, j2 = c[2]

    for i in range(n):
        for j in range(m):
            temp[i][j] = data[i][j]
            temp[i0][j0] = 1
            temp[i1][j1] = 1
            temp[i2][j2] = 1

    for i in range(n):
        for j in range(m):

            if temp[i][j] == 2:
                virus(i,j)

    l1.append(safy_space())

print(max(l1))
import sys
from collections import deque

def bfs(a,b,f):
    q = deque()
    q.append([a,b])
    count = 1
    visit = [[0]*6 for _ in range(12)]
    visit[a][b] = count

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < 12 and 0<= ny < 6:
                if ( space[nx][ny] == space[x][y] ) and ( visit[nx][ny] == 0 ):
                    count = count + 1
                    visit[nx][ny] = 1
                    q.append( [nx,ny] )

    if count > 3:
        f = f + 1
        for i in range(12):
            for j in range(6):
                if visit[i][j] == 1:
                    space[i][j] = '.'
    
    return f


def fall():
    for i in range(10,-1,-1):
        for j in range(6):
            if space[i][j] != '.' and space[i+1][j] == '.':

                for k in range(i+1,12):
                    
                    if k == 11 and space[k][j] == '.':
                        space[k][j] = space[i][j]

                    elif space[k][j] != '.':
                        space[k-1][j] = space[i][j]
                        break

                space[i][j] = '.'


space = []
for i in range(12):
    s = list(input())
    space.append(s)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0

while True:
    c = 0
    for i in range(12):
        for j in range(6):
            if space[i][j] != '.':
                c = bfs(i,j,c)

    if c == 0:
        print(answer)
        break
    else:
        answer = answer + 1
    
    fall()

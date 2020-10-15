import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0,-1,1,1,-1]
dy = [0, 0, -1, 1,-1,1,-1,1]


def bfs(x,y):
    q = deque()
    q.append([x,y])
    while(q):
        x,y = q.popleft()
        visited[x][y] = True

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= ny < w and 0<= nx < h and (space[nx][ny] == 1):
                if visited[nx][ny] == False:

                    space[nx][ny] = 0 #############################################
                    visited[nx][ny] = True 
                    q.append( [nx,ny] )


while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    space = []
    for i in range(h):
        space.append(list(map(int,input().split())))
    
    visited = [[False for i in range(w)] for i in range(h)]
    count = 0

    for i in range(h):
        for j in range(w):
            if space[i][j] == 1:
                count = count + 1
                bfs(i,j)

    print(count)
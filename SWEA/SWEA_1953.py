from collections import deque
t = int(input())
dy = [-1,1,0,0]
dx = [0,0,-1,1] # [상,하,좌,우]
for tc in range(1,t+1):
    space = []
    N, M, R, C, L = map(int,input().split())
    for i in range(N):
        space.append(list(map(int,input().split())))
    visit_check = [ [0]*M for i in range(N) ]
    q = deque()
    q.append((R,C))
    visit_check[R][C] = 1
    r_a = 0
    while (q):
        y,x = q.popleft()
        if space[y][x] == 1:
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0<= nx < M and space[ny][nx] != 0 and visit_check[ny][nx] == 0:
                    v = space[ny][nx]
                    if (i == 0 and (v == 1 or v == 2 or v == 5 or v == 6)) or (i == 1 and (v == 1 or v == 2 or v == 4 or v == 7)) or (i == 2 and (v == 1 or v == 3 or v == 4 or v == 5)) or (i == 3 and (v == 1 or v == 3 or v == 6 or v == 7)):
                        visit_check[ny][nx] = visit_check[y][x] + 1
                        q.append((ny,nx))

        elif space[y][x] == 2:
            for i in range(2):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0<= nx < M and space[ny][nx] != 0 and visit_check[ny][nx] == 0:
                    v = space[ny][nx]
                    if (i == 0 and (v == 1 or v == 2 or v == 5 or v == 6)) or (i == 1 and (v == 1 or v == 2 or v == 4 or v == 7)):
                        visit_check[ny][nx] = visit_check[y][x] + 1
                        q.append((ny,nx))

        elif space[y][x] == 3:
            for i in range(2,4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0<= nx < M and space[ny][nx] != 0 and visit_check[ny][nx] == 0:
                    v = space[ny][nx]
                    if (i == 2 and (v == 1 or v == 3 or v == 4 or v == 5)) or (i == 3 and (v == 1 or v ==  3 or v == 6 or v == 7)):
                        visit_check[ny][nx] = visit_check[y][x] + 1
                        q.append((ny,nx))

        elif space[y][x] == 4:
            for i in range(0,4,+3):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0<= nx < M and space[ny][nx] != 0 and visit_check[ny][nx] == 0:
                    v = space[ny][nx]
                    if (i == 0 and (v == 1 or v == 2 or v == 5 or v == 6)) or (i == 3 and (v == 1 or v == 3 or v == 6 or v == 7)):
                        visit_check[ny][nx] = visit_check[y][x] + 1
                        q.append((ny,nx))

        elif space[y][x] == 5:
            for i in range(1,4,+2):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0<= nx < M and space[ny][nx] != 0 and visit_check[ny][nx] == 0:
                    v = space[ny][nx]
                    if (i == 1 and (v == 1 or v == 2 or v == 4 or v == 7)) or (i == 3 and (v == 1 or v == 3 or v == 6 or v == 7)):
                        visit_check[ny][nx] = visit_check[y][x] + 1
                        q.append((ny,nx))

        elif space[y][x] == 6:
            for i in range(1,3):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0<= nx < M and space[ny][nx] != 0 and visit_check[ny][nx] == 0:
                    v = space[ny][nx]
                    if (i == 1 and (v == 1 or v == 2 or v == 4 or v == 7)) or (i == 2 and (v == 1 or v == 3 or v == 4 or v == 5)):
                        visit_check[ny][nx] = visit_check[y][x] + 1
                        q.append((ny,nx))

        elif space[y][x] == 7:
            for i in range(0,3,+2):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0<= nx < M and space[ny][nx] != 0 and visit_check[ny][nx] == 0:
                    v = space[ny][nx]
                    if (i == 0 and (v == 1 or v == 2 or v == 5 or v == 6)) or (i == 2 and (v == 1 or v == 3 or v == 4 or v == 5)):
                        visit_check[ny][nx] = visit_check[y][x] + 1
                        q.append((ny,nx))


    for i in range(N):
        for j in range(M):
            if 0 < visit_check[i][j] <= L:
                r_a += 1
        
    print('#',tc,' ',r_a,sep='')

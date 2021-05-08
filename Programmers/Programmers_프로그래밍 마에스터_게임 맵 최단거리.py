dy = [1,-1,0,0]
dx = [0,0,-1,1]
from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visit = [[False for i in range(m)] for i in range(n)]
    flag = False
    q = deque()
    q.append((0,0))
    visit[0][0] = True

    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= ny < n and 0<= nx < m and maps[ny][nx] != 0 and visit[ny][nx] == False:
                v = maps[y][x] + 1
                if maps[ny][nx] != 1:
                    maps[ny][nx] = min(v,maps[ny][nx])
                else:
                    maps[ny][nx] = v
                visit[ny][nx] = True

                q.append((ny,nx))

        if y == n-1 and x == m-1:
            flag = True
            break

    if flag :
        return maps[-1][-1]
    else:
        return -1


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
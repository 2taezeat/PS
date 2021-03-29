from collections import deque

t = int(input())
dx = [-1, 1, 1, -1]
dy = [-1, -1, 1, 1]
for test in range(1, t + 1):
    answer = -1
    n = int(input())
    map1 = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            queue = deque()
            queue.append([i, j, [map1[i][j]], 0, -1])
            while queue:
                x, y, shops, count, ld = queue.popleft()
                if x == i and y == j and count == 4:
                    if answer < len(shops):
                        answer = len(shops)
                elif count == 0:
                    nx = x + dx[2]
                    ny = y + dy[2]
                    if -1 < nx < n and -1 < ny < n and map1[nx][ny] != map1[i][j]:
                        queue.append([nx, ny, shops + [map1[nx][ny]], 1, 2])
                elif count < 5:
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if -1 < nx < n and -1 < ny < n:
                            if nx == i and ny == j and count>1:
                                if ld == d:
                                    queue.append([nx, ny, shops, count, d])
                                else:
                                    queue.append([nx, ny, shops, count + 1, d])
                            elif map1[nx][ny] not in shops:
                                if ld == d:
                                    queue.append([nx, ny, shops + [map1[nx][ny]], count, d])
                                else:
                                    queue.append([nx, ny, shops + [map1[nx][ny]], count + 1, d])
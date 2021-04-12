import sys


def solution(map1, map2, horses):
    t = 1
    while 1:

        if t > 1001:
            return -1
        for i in range(k):
            x, y, d = horses[i]
            nx = x + dx[d]
            ny = y + dy[d]
            # 파란색이거나 영역밖이면
            if not (-1 < nx < n and -1 < ny < n) or map1[nx][ny] == 2:
                d ^= 1
                nx = x + dx[d]
                ny = y + dy[d]
                if not (-1 < nx < n and -1 < ny < n) or map1[nx][ny] == 2:
                    nx = x
                    ny = y
            horses[i] = [nx, ny, d]
            if nx == x and ny == y:
                continue
            # 옮긴 뒤의 색이 하얀색
            idx = map2[x][y].index(i)
            for p in map2[x][y][idx + 1:]:
                horses[p][0] = nx
                horses[p][1] = ny
            if map1[nx][ny] == 0:
                map2[nx][ny] += map2[x][y][idx:]
            # 옮긴 뒤에 색이 빨간색
            elif map1[nx][ny] == 1:
                map2[nx][ny] += map2[x][y][idx:][::-1]
            map2[x][y] = map2[x][y][:idx]
            if len(map2[nx][ny]) > 3:
                return t
            # for O in range(n):
            #     print(map2[O])
            # print('--------------')
        t += 1


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
n, k = map(int, sys.stdin.readline().split())
map1 = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
horses = []
map2 = [[[] * n for _ in range(n)] for _ in range(n)]
for i in range(k):
    x, y, d = map(int, sys.stdin.readline().split())
    horses.append([x - 1, y - 1, d - 1])
    map2[x - 1][y - 1].append(i)
    
    # for O in range(n):
    #     print(map2[O])

    # print(horses)

ans=solution(map1,map2,horses)
print(ans)
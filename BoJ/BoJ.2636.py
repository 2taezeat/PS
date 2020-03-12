# BFS로 바깥만 탐색, 
# 네 방향중 1(치즈) -> next.append
# 네 방향중 0(빈칸) -> q.append
N, M = map(int,input().split())
space = [ list(map(int,input().split())) for i in range(N)]
time = 0
while (True):
    q = [ [0,0] ]
    nextt = []

    while (q != []):
        y,x = q.pop(0)

        for dx, dy in (0, -1), (1, 0), (0, 1), (-1, 0):
            ny = y + dy
            nx = x + dx

            if 0 <= nx < M and 0<= ny < N:
                if space[ny][nx] == 0:
                    space[ny][nx] = 5
                    q.append([ny,nx])

                if space[ny][nx] == 1:
                    space[ny][nx] = 6
                    nextt.append([ny,nx])

    # 한번의 사이클이 끝나면 nextt 체크한다.
    # 바깥쪽 치즈(1)이 없으면 종료
    if nextt == []:
        break

    lastcheeze = len(nextt)
    time = time + 1

    for y in range(N):
        for x in range(M):
            if space[y][x] == 5:
                space[y][x] = 0
            if space[y][x] == 6:
                space[y][x] = 0

print(time)
print(lastcheeze)
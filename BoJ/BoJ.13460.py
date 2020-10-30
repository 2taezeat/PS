# input 받기
from sys import stdin
from collections import deque
input = stdin.readline
n,m = map(int,input().split())
a = []
for i in range(n):
    s = list(input())
    a.append(s)

check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)] # 방문 여부를 확인할 check 배열을 4차원 배열로 선언한다. 
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1) # 배열의 인덱스는 [빨간 X좌표] [빨간 Y좌표] [파란 X좌표] [파란 Y좌표] 이다.
q = deque()

_rx, _ry, _bx, _by = [0]*4
for i in range(n):
    for j in range(m):
        if a[i][j] == 'R':
            _rx, _ry = i, j
        elif a[i][j] == 'B':
            _bx, _by = i, j
q.append((_rx, _ry, _bx, _by, 0)) # Queue에 빨간 구슬의 (X, Y) 좌표, 파란 구슬의 (X, Y) 좌표를 모두 넣는다.
check[_rx][_ry][_bx][_by] = True


# 구슬의 다음 위치가 벽이라면 앞으로 가지 못한다. 구슬의 현재 위치가 구멍이라면, 현재 구슬의 색이 무엇인지 판별한다.
def move(_x, _y, _dx, _dy, _c):
    while a[_x+_dx][_y+_dy] != '#' and a[_x][_y] != 'O': # 구슬을 굴릴 때, 구슬의 다음 위치가 벽(#)인지, 구슬의 현재 위치가 구멍(O)인지 확인한다.
        _x += _dx
        _y += _dy
        _c += 1
    return _x, _y, _c

def bfs():
    while q:
        rx, ry, bx, by, d = q.popleft()
        if d >= 10: # 굴리는 과정이 10번을 넘어가면 그대로 종료하고, -1을 출력한다.
            break

        for i in range(4):
            # 구슬을 굴리면서, 빨간 구슬의 이동 거리와 파란 구슬의 이동 거리를 카운트해야 한다.
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)

            # 구슬의 다음 위치가 벽이라면 앞으로 가지 못한다. 구슬의 현재 위치가 구멍이라면, 현재 구슬의 색이 무엇인지 판별한다.
            if a[nbx][nby] == 'O': # 만약 파란 구슬의 현재 위치가 구멍이라면 무시하고, 빨간 구슬의 현재 위치가 구멍이라면, d+1을 출력하고 종료한다.
                continue
            if a[nrx][nry] == 'O': 
                print(d+1)
                return

            # 구슬을 굴린 후, 빨간 구슬의 위치와 파란 구슬의 위치가 같다면, 이동 거리 비교를 통해 겹치지 않도록 처리해야 한다.
            if nrx == nbx and nry == nby: # 만약 구슬이 겹쳤다면, 굴릴 때 카운트했던 이동 거리가 더 긴 구슬의 위치를 한 칸 이전으로 되돌린다.
                if rc > bc:
                    nrx, nry = nrx-dx[i], nry-dy[i]
                else:
                    nbx, nby = nbx-dx[i], nby-dy[i]

                    
            if not check[nrx][nry][nbx][nby]:
                check[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, d+1)) 

    print(-1) # 굴리는 과정이 10번을 넘어가면 그대로 종료하고, -1을 출력한다. // # 더 이상 갈 곳이 없을 때에는 BFS를 빠져나와서 -1을 출력한다.


bfs()
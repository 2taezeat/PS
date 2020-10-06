import sys
from collections import deque
input = sys.stdin.readline
n,l,r = map(int,input().split())
space = []
for i in range(n):
    space.append(list(map(int,input().split())))
dx = [1,0,0,-1]
dy = [0,1,-1,0]
total_count = 0

def process(x,y,i):
    # (x,y)의 위치와 연결된 나라 정보를 담는 리스트
    united = []
    united.append((x,y))

    # bfs를 위한 q
    q = deque()
    q.append((x,y))

    union[x][y] = i # 현재 연합의 번호 할당
    summary = space[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수

    while q:
        x, y = q.popleft()

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(space[nx][ny]-space[x][y]) <= r:
                    q.append((nx,ny))
                    # 연합에 추가
                    union[nx][ny] = i
                    summary = summary + space[nx][ny]
                    count = count + 1
                    united.append((nx,ny))

    for a,b in united:
        space[a][b] = summary // count
    
    return count


# 더 이상 인구 이동을 할 수 없을 때 까지 반복 
while True:
    union = [[-1]* n for k in range(n)]
    index = 0

    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았따면
                process(i, j, index)
                index = index + 1

    if index == n*n:
        break

    total_count = total_count + 1

print(total_count)
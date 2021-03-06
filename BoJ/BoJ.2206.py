import sys
from collections import deque
n, m = map(int,input().split())
space = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    space.append(list(map(int,input())))
# 벽을 부수고 방문했는지, 그렇지 않은지에 따라 최단거리가 달라짐.
# 따라서 distance는 전자와 후자 두 가지 배열이 필요 => 3차원 배열
# distance = [][][0] 벽을 부순 상태, distance = [][][1] 벽을 부수지 않은 상태
distance = [ [ [0]*2 for j in range(m) ] for i in range(n)]
q = deque()
q.append([0, 0, 1]) # 벽을 부순적이 없는 경우로 시작
distance[0][0][1] = 1 # 처음 시작점은 방문하므로, 1로 함.

while q:
    x,y,w = q.popleft()

    # 목적지에 다달으면 break
    if x == n - 1 and y == m -1:
        break
    # 4방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
       # 좌표값이 범위가 넘지 않는 경우만을 탐색하는 if문
        if 0 <= nx < n and 0 <= ny < m:
            # 벽을 부순적이 없는 경우, 4방향 중에 벽이 있는 경우
            if space[nx][ny] == 1 and w == 1: 
                distance[nx][ny][0] = distance[x][y][1] + 1
                q.append( [nx,ny,0] ) # 이제 벽을 부수게 됨. 0 => 벽을 부순적이 있는 경우
            
            # w값은 0,1 둘 중하나가 될 수 있음. 벽을 부수적이 있는 경우(w==0), 없는 경우(w==1) 4방향 중에 벽이 없는 경우, distance[nx][ny][w] == 0 => 한 번도 방문한 적이 없는 경우
            elif space[nx][ny] == 0 and distance[nx][ny][w] == 0: 
                distance[nx][ny][w] = distance[x][y][w] + 1 
                q.append( [nx,ny,w] )

    # 벽을 부순적이 있는 경우 중에, 4방향이 모두 벽인 경우인 case는 q에 append가 이루어지지 않음.

r1, r2 = distance[n-1][m-1][0], distance[n-1][m-1][1]
if r1 == 0 and r2 == 0:
    print(-1)
else:
    print(max(r1,r2))
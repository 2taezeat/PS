import heapq
n = int(input())
space = []
for i in range(n):
    space.append(list(map(int,input().split())))
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 우선순위 : d > x > y (거리가 가장 가까운것 > 가장 위쪽 > 가장 왼쪽 순서)
q = [] # 최소 heap
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            heapq.heappush(q, (0,i,j))
            space[i][j] = 0 

body = 2 # 상어의 크기
eat = 0 # 물고기를 먹은 횟수
answer = 0 # 정답
visit = [[False]*n for i in range(n)]

while q:
    # d는 이동거리 x, y는 좌표
    d, x, y = heapq.heappop(q)

    ### 상어 크기보다 작은 크기의 물고기를 발견하면 먹는다. 먹은 칸을 0으로 바꾼다.
    if 0 < space[x][y] < body:
        eat = eat + 1
        space[x][y] = 0

        # 먹은 물고기의 갯수가 상어자신의 크기 와 같으면 크기가 1증가하고, 먹은 물고기는 다시 0으로 초기화
        if eat == body:
            body = body + 1
            eat = 0
        
        answer = answer + d # 정답에 현재까지 이동한 거리를 더함.
        d = 0 # 이동한 거리 d를 0으로 초기화

        # 이미 갔던 곳(visit = True)을 물고기를 먹기 위해 움직이는 동안 다시 방문할수 있으므로, visit를 다시 초기화 하고, q를 비운다.
        while q:
            q.pop()
        
        visit = [[False]*n for i in range(n)]
    ###

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        nd = d + 1

        if 0 <= nx < n and 0 <= ny < n:
            if visit[nx][ny] == False and space[nx][ny] <= body :
                visit[nx][ny] = True # 방문하였다고 update함.
                heapq.heappush(q, (nd, nx, ny) )

print(answer)
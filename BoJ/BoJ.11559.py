import sys
from collections import deque

def bfs(a,b,f):
    q = deque()
    q.append([a,b])
    count = 1
    visit = [[0]*6 for _ in range(12)]
    visit[a][b] = count

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < 12 and 0<= ny < 6:
                if ( space[nx][ny] == space[x][y] ) and ( visit[nx][ny] == 0 ): # 방문한 곳이 아니고, 같은 뿌요 일 때
                    count = count + 1
                    visit[nx][ny] = 1
                    q.append( [nx,ny] )

    if count > 3: # 모인 뿌요의 갯수가 4이상이 되면
        f = f + 1
        for i in range(12):
            for j in range(6):
                if visit[i][j] == 1: # 방문한 곳을 '.' 로 바꿈.
                    space[i][j] = '.'
    
    return f

# 뿌요의 바로 아래에 . 이 있으면 떨어져야 하므로 다른 뿌요가 있거나 바닥에 닿을 때 까지 뿌요를 떨어뜨린다.
def fall():
    for i in range(10,-1,-1):
        for j in range(6):
            if space[i][j] != '.' and space[i+1][j] == '.':

                for k in range(i+1,12):
                    
                    if k == 11 and space[k][j] == '.':
                        space[k][j] = space[i][j]

                    elif space[k][j] != '.':
                        space[k-1][j] = space[i][j]
                        break

                space[i][j] = '.'

space = []
for i in range(12):
    s = list(input())
    space.append(s)

# 상, 하, 좌, 우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0

while True:
    c = 0
    for i in range(12):
        for j in range(6):
            if space[i][j] != '.':
                c = bfs(i,j,c)

    if c == 0: # bfs 탐색으로 4개 이상의 뿌요가 모인 경우를 찾지 못한 경우는 'answer'을 출력 한다. 
        print(answer)
        break
    else: 
        answer = answer + 1 # 4개 이상 찾은 경우는 answer + 1 한다.
    
    fall() # fall 함수 호출.
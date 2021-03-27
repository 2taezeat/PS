import sys
N = int(sys.stdin.readline())
space = []
for i in range(N):
    space.append(list(map(int,sys.stdin.readline().split())))
answer = 0

def dfs(y,x,shape):
    global answer
    if y == N-1 and x == N-1:
        answer += 1
    
    if shape == 1:
        ny2 = y
        nx2 = x + 1
        if 0 <= ny2 < N and 0 <= nx2 < N and space[ny2][nx2] == 0 :
            dfs(ny2,nx2,1)
        ny4 = y + 1
        nx4 = x + 1
        if 0 <= ny4 < N and 0 <= nx4 < N and space[ny4][nx4] == 0 and space[ny4][nx4-1] == 0 and space[ny4-1][nx4] == 0 :
            dfs(ny4,nx4,2)

    elif shape == 2:
        ny2 = y
        nx2 = x + 1
        if 0 <= ny2 < N and 0 <= nx2 < N and space[ny2][nx2] == 0 :
            dfs(ny2,nx2,1)
        ny4 = y + 1
        nx4 = x
        if 0 <= ny4 < N and 0 <= nx4 < N and space[ny4][nx4] == 0 :
            dfs(ny4,nx4,3)
        ny6 = y + 1
        nx6 = x + 1
        if 0 <= ny6 < N and 0 <= nx6 < N and space[ny6][nx6] == 0 and space[ny6][nx6-1] == 0 and space[ny6-1][nx6] == 0:
            dfs(ny6,nx6,2)

    elif shape == 3:
        ny2 = y + 1
        nx2 = x
        if 0 <= ny2 < N and 0 <= nx2 < N and space[ny2][nx2] == 0 :
            dfs(ny2,nx2,3)
        ny4 = y + 1
        nx4 = x + 1
        if 0 <= ny4 < N and 0 <= nx4 < N and space[ny4][nx4] == 0 and space[ny4][nx4-1] == 0 and space[ny4-1][nx4] == 0 :
            dfs(ny4,nx4,2)

if space[-1][-1] == 1:
    print(0)
else:
    dfs(0,1,1)
    print(answer)
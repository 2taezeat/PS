import sys
#input = sys.stdin.readline

N , M = map(int,input().split())
space = [ [3] * M for i in range(N)]

for i in range(N):
    l1 = list(map(int,input()))
    space[i] = l1

dx = [0, 1 , 0 ,-1 ] #위, 오른쪽, 아래, 왼쪽
dy = [-1, 0, 1,  0]

def bfs(y,x):
    global space
    q = [ [y,x] ]
    while ( q != [] ):
        now = q.pop(0)

        for i in range(4):
            nowx = now[1] + dx[i]
            nowy = now[0] + dy[i]

            if 0 <= nowx < M and 0<= nowy < N and space[nowy][nowx] == 1:
                #space[nowy][nowx] = space[nowy][nowx] + 1
                space[nowy][nowx] = space[now[0]][now[1]] + 1
                q.append( [nowy,nowx] ) 

bfs(0,0)
print(space[-1][-1])
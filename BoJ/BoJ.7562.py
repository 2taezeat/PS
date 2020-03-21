dx = [-2,-1,1,2,2,1,-1,-2]
dy = [-1,-2,-2,-1,1,2,2,1]

def bfs(y,x,space,I,goaly,goalx):
    c = 0
    q = [ [y,x],[10000,10000] ]
    while ( q != [] ):
        now = q.pop(0)

        for k in range(8):
            nowx = now[1] + dx[k]
            nowy = now[0] + dy[k]

            if 0 <= nowx < I and 0<= nowy < I and space[nowy][nowx] == 0:
                space[nowy][nowx] = space[now[0]][now[1]] + 1

                if nowy == goaly and nowx == goalx:
                    return space[goaly][goalx]
                
                q.append( [nowy,nowx] )

T = int(input())
for t in range(T):
    i = int(input())
    space = [[0]*i for _ in range(i) ]
    ny,nx = map(int,input().split())
    goaly, goalx = map(int,input().split())
    
    if ny == goaly and nx == goalx:
        print(0)
    else:
        a = bfs(ny,nx,space,i,goaly,goalx)
        print(a)
dy = [1,-1,0,0]
dx = [0,0,-1,1]
fc = float('inf')

def solution(board):
    N = len(board)
    cost = [[float('inf') for _ in range(N)] for _ in range(N)]
    dfs(0,0,board,0,0,cost)
    return (fc-5)*100

def dfs(y,x,board,pre_dire,g,cost):
    global fc
    N = len(board)    

    if g > fc:
        return # 비용이 fc를 넘어가면 컷.

    if cost[y][x] < g: # 현재좌표의 비용이 g를 넘어가면 컷. 정답이 될 수 없기에.
        return

    elif cost[y][x] >= g: # 그게 아니면, 갱신.
        cost[y][x] = g

    if y == N-1 and x == N-1:
        fc = cost[-1][-1] # 목적지 도달하면, fc 갱신
        return 

    board[y][x] = 2

    if 0<= y < N and 0<= x+1 < N and board[y][x+1] == 0 :
        if pre_dire != 1:
            dfs(y,x+1,board,1,g+6,cost)
        else:
            dfs(y,x+1,board,1,g+1,cost)

    if 0<= y+1 < N and 0<= x < N and board[y+1][x] == 0 :
        if pre_dire != 4:
            dfs(y+1,x,board,4,g+6,cost)
        else:
            dfs(y+1,x,board,4,g+1,cost)

    if 0<= y-1 < N and 0<= x < N and board[y-1][x] == 0 :
        if pre_dire != 3:
            dfs(y-1,x,board,3,g+6,cost)
        else:
            dfs(y-1,x,board,3,g+1,cost)

    if 0<= y < N and 0<= x-1 < N and board[y][x-1] == 0 :
        if pre_dire != 2:
            dfs(y,x-1,board,2,g+6,cost)
        else:
            dfs(y,x-1,board,2,g+1,cost)

    board[y][x] = 0

#print(solution([[0,0,0],[0,0,0],[0,0,0]]))
#print (solution(   [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]    ) )
#print( solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
#print( solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
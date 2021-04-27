board = [[0,0,0],[0,0,0],[0,0,0]]


def dfs(y,x,board):
    N = len(board)
    

    if y == N-1 and x == N-1:
        return

    visited[y][x] = 1 # 방문 했음.
    board[y][x] = 2
    print(board)

    if 0<= y < N and 0<= x+1 < N and board[y][x+1] != 1 and visited[y][x+1] == 0:
        dfs(y,x+1,board)

    if 0<= y < N and 0<= x-1 < N and board[y][x-1] != 1 and visited[y][x-1] == 0:
        dfs(y,x-1,board)

    if 0<= y-1 < N and 0<= x < N and board[y-1][x] != 1 and visited[y-1][x] == 0:
        dfs(y-1,x,board)
    
    if 0<= y+1 < N and 0<= x < N and board[y+1][x] != 1 and visited[y+1][x] == 0:
        dfs(y+1,x,board)

    visited[y][x] = 0
    board[y][x] = 0

visited = [[0 for _ in range(3)] for _ in range(3)]
dfs(0,0,board)


dy = [1,-1,0,0]
dx = [0,0,-1,1]
fc = 9999999999

def solution(board):
    dfs(0,0,board,[])
    return fc

def cost_cal(w):
    cost = 100 * len(w)
    count_90_f = 0
    for g in range( 0, len(w)-1 ):
        if w[g] != w[g+1]:
            count_90_f += 1
    cost = cost + (count_90_f * 500)
    return cost

def dfs(y,x,board,wkcnl):
    global fc
    N = len(board)
    
    if y == N-1 and x == N-1:
        final_cost = cost_cal(wkcnl)        
        fc = min(final_cost, fc)
        return fc

    board[y][x] = 2

    ccc = cost_cal(wkcnl)
    if ccc > fc :
        board[y][x] = 0
        return

    if 0<= y < N and 0<= x+1 < N and board[y][x+1] == 0 :
        wkcnl.append(1)
        dfs(y,x+1,board,wkcnl)
        wkcnl.pop()

    if 0<= y < N and 0<= x-1 < N and board[y][x-1] == 0 :
        wkcnl.append(2)
        dfs(y,x-1,board,wkcnl)
        wkcnl.pop()

    if 0<= y-1 < N and 0<= x < N and board[y-1][x] == 0 :
        wkcnl.append(3)
        dfs(y-1,x,board,wkcnl)
        wkcnl.pop()
    
    if 0<= y+1 < N and 0<= x < N and board[y+1][x] == 0 :
        wkcnl.append(4)
        dfs(y+1,x,board,wkcnl)
        wkcnl.pop()

    board[y][x] = 0


print (solution(   [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]    ) )
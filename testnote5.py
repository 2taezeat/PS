dy = [1,-1,0,0]
dx = [0,0,-1,1]
fc = 9999999999

def solution(board):
    global answer
    N = len(board)
    cost = [[INF for _ in range(N)] for _ in range(N)]
    dfs(0,0,board,0,0,cost)
    return (fc)

def cost_cal(w,gg):
    cost = 100 * len(w)
    cost = cost + (gg * 500)
    return cost

def dfs(y,x,board,wkcnl,pre_dire,g,cost):
    global fc
    N = len(board)
    
    if y == N-1 and x == N-1:
        # final_cost = cost_cal(wkcnl,g)        
        # fc = min(final_cost, fc)
        return 

    board[y][x] = 2

    # ccc = cost_cal(wkcnl,g)
    # if ccc > fc :
    #     board[y][x] = 0
    #     return

    if 0<= y < N and 0<= x+1 < N and board[y][x+1] == 0 :
        #wkcnl.append(1)
        if pre_dire != 1:
            dfs(y,x+1,board,1,g+6)
        else:
            dfs(y,x+1,board,1,g+1)
        #wkcnl.pop()

    if 0<= y+1 < N and 0<= x < N and board[y+1][x] == 0 :
        #wkcnl.append(4)
        if pre_dire != 4:
            dfs(y+1,x,board,4,g+6)
        else:
            dfs(y+1,x,board,4,g+1)
        #wkcnl.pop()

    if 0<= y-1 < N and 0<= x < N and board[y-1][x] == 0 :
        #wkcnl.append(3)
        if pre_dire != 3:
            dfs(y-1,x,board,3,g+6)
        else:
            dfs(y-1,x,board,3,g+1)
        #wkcnl.pop()

    if 0<= y < N and 0<= x-1 < N and board[y][x-1] == 0 :
        #wkcnl.append(2)
        if pre_dire != 2:
            dfs(y,x-1,board,2,g+6)
        else:
            dfs(y,x-1,board,2,g+1)
        #wkcnl.pop()

    board[y][x] = 0

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
#print (solution(   [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]    ) )
#print( solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))

#print( solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
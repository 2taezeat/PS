dy = [1,-1,0,0]
dx = [0,0,-1,1]
fc = 9999999999

def solution(board):
    dfs(0,0,board,[],0)
    return fc

def cost_cal(w,g):
    print(w,g)
    cost = 100 * len(w)
    cost = cost + (g * 500)
    return cost

def dfs(y,x,board,wkcnl,g):
    global fc
    N = len(board)

    ccc = cost_cal(wkcnl,g)
    if ccc > fc :
        board[y][x] = 0
        return
    
    if y == N-1 and x == N-1:
        final_cost = cost_cal(wkcnl,g)        
        fc = min(final_cost, fc)
        return fc

    board[y][x] = 2


    if 0<= y < N and 0<= x+1 < N and board[y][x+1] == 0 :
        if wkcnl != []:
            if wkcnl[-1] == 2 or wkcnl[-1] == 3 or wkcnl[-1] == 4:
                wkcnl.append(1)
                dfs(y,x+1,board,wkcnl,g+1)
            else:
                wkcnl.append(1)
                dfs(y,x+1,board,wkcnl,g)

        wkcnl.pop()

    if 0<= y < N and 0<= x-1 < N and board[y][x-1] == 0 :
        if wkcnl != []:
            if wkcnl[-1] == 1 or wkcnl[-1] == 3 or wkcnl[-1] == 4:
                wkcnl.append(2)
                dfs(y,x-1,board,wkcnl,g+1)
            else:
                wkcnl.append(2)
                dfs(y,x-1,board,wkcnl,g)

        wkcnl.pop()

    if 0<= y-1 < N and 0<= x < N and board[y-1][x] == 0 :
        if wkcnl != []:
            if wkcnl[-1] == 1 or wkcnl[-1] == 2 or wkcnl[-1] == 4:
                wkcnl.append(3)
                dfs(y-1,x,board,wkcnl,g+1)
            else:
                wkcnl.append(3)
                dfs(y-1,x,board,wkcnl,g)
        wkcnl.pop()
    
    if 0<= y+1 < N and 0<= x < N and board[y+1][x] == 0 :
        if wkcnl != []:
            if wkcnl[-1] == 1 or wkcnl[-1] == 2 or wkcnl[-1] == 3:
                wkcnl.append(4)
                dfs(y+1,x,board,wkcnl,g+1)
            else:
                wkcnl.append(4)
                dfs(y+1,x,board,wkcnl,g)
        wkcnl.pop()

    board[y][x] = 0

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
#print (solution(   [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]    ) )
#print( solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
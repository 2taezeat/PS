dy = [1,-1,0,0]
dx = [0,0,-1,1]
result = []

def solution(board):
    dfs(0,0,board,[])

    return min(result)


def dfs(y,x,board,wkcnl):
    global result
    N = len(board)
    
    if y == N-1 and x == N-1:
        print(wkcnl)
        cost = 100*len(wkcnl)
        count_90 = 0
        for g in range( 0, len(wkcnl)-1 ):
            if wkcnl[g] != wkcnl[g+1]:
                count_90 += 1

        cost = cost + (count_90 * 500)
        result.append(cost)

        return 

    board[y][x] = 2

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
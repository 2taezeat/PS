board = [[0,0,0],[0,0,0],[0,0,0]]
gnqh = []
result = []

def dfs(y,x,board,wkcnl):
    global gnqh
    N = len(board)
    
    if y == N-1 and x == N-1:
        for i in range(3):
            print(board[i])
        print(wkcnl)
        print('------------')


        for g in wkcnl:
            print(g)


        gnqh.append(wkcnl)
        #gnqh.append(123)
        return gnqh

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

#visited = [[0 for _ in range(3)] for _ in range(3)]

aa = dfs(0,0,board,[])
print(aa)
for g in aa:
    print(g)
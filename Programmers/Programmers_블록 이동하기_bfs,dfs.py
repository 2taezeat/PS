from collections import deque

def get_next_pos(pos,board):
    next_pos = [] # 반환 결과 ( 이동 가능한 위치들 )
    pos = list(pos) # 현재 위치 정보를 리스트로 변환(집합 -> 리스트)
    dx = [1,0,-1,0] 
    dy = [0,-1,0,1]
    pos1_x, pos1_y = pos[0][0], pos[0][1]
    pos2_x, pos2_y = pos[1][0], pos[1][1]
    for i in range(4):
        pos1_n_x, pos1_n_y = pos1_x + dx[i], pos1_y + dy[i]
        pos2_n_x, pos2_n_y = pos2_x + dx[i], pos2_y + dy[i]

        # 이동
        # 이동 하고자 하는 두칸이 모두 비어 있다면
        if board[pos1_n_x][pos1_n_y] == 0 and board [pos2_n_x][pos2_n_y] == 0:
            next_pos.append( { ( pos1_n_x, pos1_n_y ), ( pos2_n_x, pos2_n_y ) } )

    # 회전
    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x :
        for i in [-1,1]:
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0 :  # 위쪽 혹은 아래쪽 두칸이 모두 비어 있다면
                next_pos.append( { ( pos1_x, pos1_y ), ( pos1_x + i, pos1_y ) } )
                next_pos.append( { ( pos2_x, pos2_y ), ( pos2_x + i, pos2_y ) } )
        
    # 현재 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y :
        for i in [-1,1]:
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0 : # 왼쪽 혹은 오른쪽 두칸이 모두 비어 있다면
                next_pos.append( { ( pos1_x, pos1_y ), ( pos1_x, pos1_y + i ) } )
                next_pos.append( { ( pos2_x, pos2_y ), ( pos2_x, pos2_y + i ) } )

    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos


def solution(board):
    n = len(board)
    space = [[1] * (n+2) for i in range(n+2)]

    for i in range(n):
        for j in range(n):
            space[i+1][j+1] = board[i][j]
    
    q = deque()
    visited = []
    pos = {(1,1),(1,2)} # set, 시작위치 설정
    q.append ( ( pos, 0 ) )
    visited.append(pos)

    while q:
        pos, cost = q.popleft()        
        getn_p = get_next_pos(pos, space)

        for n_p in getn_p:
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if n_p not in visited:
                q.append( ( n_p, cost + 1 ) )
                visited.append(n_p)
        
        #     print(pos,cost)
        # print('-------------------')
        if (n,n) in pos:
            return cost

    return 0


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))

def solution(board):
    answer = 0
    for i in range(len(board)):
        answer = answer + sum(board[i][:])

    if answer == 0:
        return 0

    answer = 0
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] == 0:
                continue
            else:
                a = min(board[i-1][j], board[i-1][j-1], board[i][j-1])
                board[i][j] = a + 1

            answer = max(answer, board[i][j])

    if answer == 0:
        return 1

    return (answer ** 2)

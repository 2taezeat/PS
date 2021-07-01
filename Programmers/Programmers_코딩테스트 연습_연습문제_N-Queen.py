import itertools
def solution(n):

    board = []

    for i in range(1,n+1):
        for j in range(1,n+1):
            board.append((i,j))

    #print(board)

    c = list(itertools.combinations(board,n))
    #print(c)
    print(len(c))


    answer = 0
    return answer


print(solution(12))
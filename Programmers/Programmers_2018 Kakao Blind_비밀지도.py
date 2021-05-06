def solution(n, arr1, arr2):
    board = [ [' ' for i in range(n)] for i in range(n)]
    for i in range(n):
        b = bin(arr1[i])
        b = list(b[2:])
        
        c = n - len(b)
        for _ in range(c):
            b.insert(0,'0')
        
        for j in range(len(b)):
            if b[j] == '1':
                board[i][j] = '#'

    for i in range(n):
        b = bin(arr2[i])
        b = list(b[2:])
        
        c = n - len(b)
        for _ in range(c):
            b.insert(0,'0')
        
        for j in range(len(b)):
            if b[j] == '1':
                board[i][j] = '#'

    answer = []

    for i in range(n):
        answer.append(''.join(board[i]))
    return answer


print(solution(5,	[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
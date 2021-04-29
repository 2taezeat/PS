def solution(rows, columns, queries):
    board = [ [0 for i in range(columns)] for i in range(rows)]
    result = []
    c = 0
    while(c < columns*rows):
        i = c % columns
        j = c // columns
        board[j][i] = c + 1
        c = c + 1

    for x1,y1,x2,y2 in queries:
        x1 = x1 - 1
        y1 = y1 - 1
        x2 = x2 - 1
        y2 = y2 - 1
        l1,l2,l3,l4 = [],[],[],[]
        for i in range(y1,y2):
            l1.append(board[x1][i])
        for i in range(x2,x1,-1):
            l3.append(board[i][y1])
        for i in range(y2,y1,-1):
            l2.append(board[x2][i])
        for i in range(x1,x2):
            l4.append(board[i][y2])

        m1 = min(l1)
        m2 = min(l2)
        m3 = min(l3)
        m4 = min(l4)
        final_m = min(m1,m2,m3,m4)
        result.append(final_m)

        i1 = y1+1
        idx1 = 0
        while(i1 < y2+1):
            board[x1][i1] = l1[idx1]
            idx1 += 1
            i1 += 1
        i4 = x1+1
        idx4 = 0
        while(i4 < x2+1):
            board[i4][y2] = l4[idx4]
            idx4 += 1
            i4 += 1
        i2 = y2-1
        idx2 = 0
        while(i2 > y1-1):
            board[x2][i2] = l2[idx2]
            idx2 += 1
            i2 -= 1

        i3 = x2-1
        idx3 = 0
        while(i3 > x1-1):
            board[i3][y1] = l3[idx3]
            idx3 += 1
            i3 -= 1

    return result


print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
#print(solution(6,6,[[2,2,5,4]]))
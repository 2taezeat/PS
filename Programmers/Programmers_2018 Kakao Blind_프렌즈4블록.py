def solution(m, n, board):
    answer = 0
    space = []
    for i in range(m): space.append( list(board[i]) )

    while(1):
        T = 0
        l1 = set()
        for i in range(0,m-1):
            for j in range(0,n-1):
                sta = space[i][j]
                if space[i][j] == sta and space[i+1][j] == sta and space[i][j+1] == sta and space[i+1][j+1] == sta and sta != 0:
                    l1.add((i,j))
                    l1.add((i,j+1))
                    l1.add((i+1,j))
                    l1.add((i+1,j+1))
                    T = T + 1

        l1 = list(l1)
        answer += len(l1)
        for (y,x) in l1:
            space[y][x] = 0
        
        for j in range(0,n):
            tmp = []
            zero_count = 0
            semi = []
            for i in range(0,m): tmp.append( space[i][j] )

            for t in range(len(tmp)):
                if tmp[t] == 0: zero_count += 1
                else: semi.append(tmp[t])
            for _ in range(zero_count): semi.insert(0,0)
            for s in range(len(semi)): space[s][j] = semi[s]
                
        if T == 0:
            break
        

    return answer


#print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
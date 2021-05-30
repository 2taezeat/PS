def solution(m, n, puddles):
    space = [ [ 0 for i in range(m+1) ] for i in range(n+1)]    
    space[1][1] = 1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j,i] in puddles or (i==1 and j==1):
                continue
            
            space[i][j] = space[i][j-1] + space[i-1][j]

    return space[-1][-1] % 1000000007
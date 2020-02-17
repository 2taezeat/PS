N, M = map( int ,input().split() )
r,c,d = map( int ,input().split() )
space = []
for i in range(N):
    a =  list ( map( int ,input().split() ))
    space.append(a)

def asd(r,c,d,count,space):
    #1 현재 위치를 청소한다.
    if space[r][c] != 1:
        space[r][c] = 3
        count = count + 1

    #2 현재위치에서 현재 방향(d)을 기준으로 왼쪽방향 탐색
    if d == 0: # 방향이 북쪽일때,
        if (space[r][c-1] != 0 ) and (space[r-1][c] != 0 ) and (space[r][c+1] != 0 ) and (space[r+1][c] != 0 ):

            if (space[r+1][c] == 1):
                return count
            else:
                r = r + 1
                count = count - 1
                return asd(r,c,d,count,space)

        else:
            if space[r][c-1] == 0:
                d = 3
                c = c - 1
                return asd(r,c,d,count,space)
            if space[r][c-1] == 1 or space[r][c-1] == 3:
                d = 3 # 북에서 서(왼쪽방향)
                count = count - 1
                return asd(r,c,d,count,space)

    if d == 1: # 방향이 동쪽일때,
        if (space[r][c-1] != 0 ) and (space[r-1][c] != 0 ) and (space[r][c+1] != 0 ) and (space[r+1][c] != 0 ):

            if ( space[r][c-1] == 1 ):
                return count
            else:
                c = c - 1
                count = count - 1
                return asd(r,c,d,count,space)

        else:
            if space[r-1][c] == 0:
                d = 0
                r = r - 1
                return asd(r,c,d,count,space)
            if space[r-1][c] == 1 or space[r-1][c] == 3:
                d = 0
                count = count - 1
                return asd(r,c,d,count,space)
            
    if d == 2: # 방향이 남쪽일때,
        if (space[r][c-1] != 0 ) and (space[r-1][c] != 0 ) and (space[r][c+1] != 0 ) and (space[r+1][c] != 0 ):

            if ( space[r-1][c] == 1 ):
                return count
            else:
                r = r - 1
                count = count - 1
                return asd(r,c,d,count,space)
                
        else:
            if space[r][c+1] == 0:
                d = 1
                c = c + 1
                return asd(r,c,d,count,space)
            if space[r][c+1] == 1 or space[r][c+1] == 3:
                d = 1 # 
                count = count - 1
                return asd(r,c,d,count,space)

    if d == 3: # 방향이 서쪽일때,
        if (space[r][c-1] != 0 ) and (space[r-1][c] != 0 ) and (space[r][c+1] != 0 ) and (space[r+1][c] != 0 ):

            if ( space[r][c+1] == 1 ):
                return count
            else:
                c = c + 1
                count = count - 1
                return asd(r,c,d,count,space)

        else:
            if space[r+1][c] == 0:
                d = 2
                r = r + 1
                return asd(r,c,d,count,space)
            if space[r+1][c] == 1 or space[r+1][c] == 3:
                d = 2 # 
                count = count - 1
                return asd(r,c,d,count,space)

r = asd(r,c,d,0,space)
print(r)
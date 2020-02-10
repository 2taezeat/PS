N, M = map( int ,input().split() )
r,c,d = map( int ,input().split() )
space = []
for i in range(N):
    a =  list ( map( int ,input().split() ))
    space.append(a)
print(space)

def asd(r,c,d,count,space):
    #1 현재 위치를 청소한다.
    if space[r][c] == 1:
        pass
    else:
        space[r][c] = 3
        count = count + 1
    print('-'*15)
    print(count)
    print(r,c,d)
    print(space)
    print('-'*15)
    #2 현재위치에서 현재 방향(d)을 기준으로 왼쪽방향 탐색
    
    if d == 0: # 방향이 북쪽일때,
        # 2-1 
        if space[r][c-1] == 0:
            d = 3
            c = c - 1
            asd(r,c,d,count,space)
        
        # 2- b    
        elif space[r][c-1] == 1:
            d = 3 # 북에서 서(왼쪽방향)
            count = count - 1
            asd(r,c,d,count,space)
        #2 - c
        elif (space[r][c-1] == 3 or 1) and (space[r-1][c] == 3 or 1) and (space[r][c+1] == 3 or 1) and (space[r+1][c] == 3 or 1) and (r+1 != 1):
            print(123123)
            d = d
            r = r + 1
            count = count - 1
            asd(r,c,d,count,space)
        # 2 -d 
        elif (space[r][c-1] == 3 or 1) and (space[r-1][c] == 3 or 1) and (space[r][c+1] == 3 or 1) and (space[r+1][c] == 3 or 1) and ( r+1 == 1 ):
            return count

    if d == 1: # 방향이 동쪽일때,
        if space[r-1][c] == 0:
            d = 0
            r = r - 1
            asd(r,c,d,count,space)
        # 2- b    
        elif space[r-1][c] == 1:
            d = 0 # 
            count = count - 1
            asd(r,c,d,count,space)
        #2 - c
        elif (space[r][c-1] == 3 or 1) and (space[r-1][c] == 3 or 1) and (space[r][c+1] == 3 or 1) and (space[r+1][c] == 3 or 1) and (c -1 != 1):
            d = d
            c = c - 1
            count = count - 1
            asd(r,c,d,count,space)
        # 2 -d 
        elif (space[r][c-1] == 3 or 1) and (space[r-1][c] == 3 or 1) and (space[r][c+1] == 3 or 1) and (space[r+1][c] == 3 or 1) and ( c - 1 == 1 ):
            return count
            
    if d == 2: # 방향이 남쪽일때,
        if space[r][c+1] == 0:
            d = 1
            c = c + 1
            asd(r,c,d,count,space)
        # 2- b    
        elif space[r][c+1] == 1:
            d = 1 # 
            count = count - 1
            asd(r,c,d,count,space)
        #2 - c
        elif (space[r][c-1] == 3 or 1) and (space[r-1][c] == 3 or 1) and (space[r][c+1] == 3 or 1) and (space[r+1][c] == 3 or 1) and ( r - 1 != 1 ):
            d = d
            r = r - 1
            count = count - 1
            asd(r,c,d,count,space)
        # 2 -d 
        elif (space[r][c-1] == 3 or 1) and (space[r-1][c] == 3 or 1) and (space[r][c+1] == 3 or 1 ) and (space[r+1][c] == 3 or 1) and ( r - 1 == 1 ):
            return count

    if d == 3: # 방향이 서쪽일때,
        if space[r+1][c] == 0:
            d = 2
            r = r + 1
            asd(r,c,d,count,space)
        # 2- b    
        elif space[r+1][c] == 1:
            d = 2 # 
            count = count - 1
            asd(r,c,d,count,space)
        #2 - c
        elif (space[r][c-1] == 3 or 1) and (space[r-1][c] == 3 or 1) and (space[r][c+1] == 3 or 1) and (space[r+1][c] == 3 or 1) and ( c + 1 != 1 ):
            d = d
            c = c + 1
            count = count - 1
            asd(r,c,d,count,space)
        # 2 -d 
        elif (space[r][c-1] == 3 or 1) and (space[r-1][c] == 3 or 1) and (space[r][c+1] == 3 or 1) and (space[r+1][c] == 3 or 1) and ( c + 1 == 1 ):
            return count

r = asd(r,c,d,1,space)
print(space)
print(r)
import copy
N, K = map(int,input().split())
space_color = [[2]*(N+2) ]
dy = [99,0,0,-1,1]
dx = [99,1,-1,0,0]
for i in range(N):
    a = [2]
    a = a + list ( map(int,input().split()) )
    a = a + [2]
    space_color.append( a )
space_color.append([2]*(N+2) )
akf = [[[] * (N+2) for i in range(N+2)] for i in range(N+2)]
for i in range(1,K+1):
    y,x,d = map(int,input().split())
    akf[y][x].append( [i,d,y,x] )

for turn in range(1,1001):
    for indx in range(1,K+1):
        
        for b in range(1,N+1):
            for a in range(1,N+1):
                for (i0,d0,y0,x0) in akf[b][a]:
                    if i0 == indx:
                        reve = copy.deepcopy(akf[b][a])
                        break

        for idx in range(len(reve)):
            if reve[idx][0] == indx:
                z = idx
                break

        i = reve[z][0]
        d = reve[z][1]
        y = reve[z][2]
        x = reve[z][3]

        for o in range( len(akf[y][x])-z ):
            akf[y][x].pop()

        if d == 1:
            ny = y + dy[1]
            nx = x + dx[1] # <-
            if space_color[ny][nx] == 0:
                for (I,D,Y,X) in reve[z:]:
                    akf[ny][nx].append([I,D,Y+dy[1],X+dx[1]])
        
            elif space_color[ny][nx] == 1:
                for (I,D,Y,X) in reve[z:][::-1]:
                    akf[ny][nx].append([I,D,Y+dy[1],X+dx[1]])


            elif space_color[ny][nx] == 2:
                d = 2 # 벽 붙히져서 다시 원래 재 자리로 이동 // <-, 제자리
                ny = ny + dy[2]
                nx = nx + dx[2]
                ny2 = ny + dy[2] # 제자리에서 다시 움직임. <-, 제자리, ->
                nx2 = nx + dx[2]

                if space_color[ny2][nx2] == 0:
                    for (I,D,Y,X) in reve[z:]:
                        if I == i:
                            akf[ny2][nx2].append( [i,2,ny2,nx2] )
                        else:
                            akf[ny2][nx2].append([I,D,Y+dy[2],X+dx[2]])

                elif space_color[ny2][nx2] == 1:
                    for (I,D,Y,X) in reve[z:][::-1]:
                        if I == i:
                            akf[ny2][nx2].append( [i,2,ny2,nx2] )
                        else:
                            akf[ny2][nx2].append([I,D,Y+dy[2],X+dx[2]])

                elif space_color[ny2][nx2] == 2:
                    ny3 = ny2 + dy[1] # <-, '제자리', ->, 다시 '제자리', 방향은 안바꿈
                    nx3 = nx2 + dx[1]
                    for (I,D,Y,X)  in reve[z:]:
                        if I == i:
                            akf[ny3][nx3].append( [i,2,ny3,nx3] )
                        else:
                            akf[ny3][nx3].append([I,D,Y,X])

        elif d == 2:
            ny = y + dy[2]
            nx = x + dx[2] # <-

            if space_color[ny][nx] == 0:
                for (I,D,Y,X) in reve[z:]:
                    akf[ny][nx].append([I,D,Y+dy[2],X+dx[2]])
            elif space_color[ny][nx] == 1:
                for (I,D,Y,X) in reve[z:][::-1]:
                    akf[ny][nx].append([I,D,Y+dy[2],X+dx[2]])


            elif space_color[ny][nx] == 2:
                d = 1 # 벽 붙히져서 다시 원래 재 자리로 이동 // <-, 제자리
                ny = ny + dy[1]
                nx = nx + dx[1]
                ny2 = ny + dy[1] # 제자리에서 다시 움직임. <-, 제자리, ->
                nx2 = nx + dx[1]

                if space_color[ny2][nx2] == 0:
                    for (I,D,Y,X) in reve[z:]:
                        if I == i:
                            akf[ny2][nx2].append( [i,1,ny2,nx2] )
                        else:
                            akf[ny2][nx2].append([I,D,Y+dy[1],X+dx[1]])

                elif space_color[ny2][nx2] == 1:
                    for (I,D,Y,X) in reve[z:][::-1]:
                        if I == i:
                            akf[ny2][nx2].append( [i,1,ny2,nx2] )
                        else:
                            akf[ny2][nx2].append([I,D,Y+dy[1],X+dx[1]])

                elif space_color[ny2][nx2] == 2:
                    ny3 = ny2 + dy[2] # <-, '제자리', ->, 다시 '제자리', 방향은 안바꿈
                    nx3 = nx2 + dx[2]
                    for (I,D,Y,X)  in reve[z:]:
                        if I == i:
                            akf[ny3][nx3].append( [i,1,ny3,nx3] )
                        else:
                            akf[ny3][nx3].append([I,D,Y,X])

        elif d == 3:
            ny = y + dy[3]
            nx = x + dx[3] # <-

            if space_color[ny][nx] == 0:
                for (I,D,Y,X) in reve[z:]:
                    akf[ny][nx].append([I,D,Y+dy[3],X+dx[3]])
            elif space_color[ny][nx] == 1:
                for (I,D,Y,X) in reve[z:][::-1]:
                    akf[ny][nx].append([I,D,Y+dy[3],X+dx[3]])

            elif space_color[ny][nx] == 2:
                d = 4 # 벽 붙히져서 다시 원래 재 자리로 이동 // <-, 제자리
                ny = ny + dy[4]
                nx = nx + dx[4]
                ny2 = ny + dy[4] # 제자리에서 다시 움직임. <-, 제자리, ->
                nx2 = nx + dx[4]

                if space_color[ny2][nx2] == 0:
                    for (I,D,Y,X) in reve[z:]:
                        if I == i:
                            akf[ny2][nx2].append( [i,4,ny2,nx2] )
                        else:
                            akf[ny2][nx2].append([I,D,Y+dy[4],X+dx[4]])

                elif space_color[ny2][nx2] == 1:
                    for (I,D,Y,X) in reve[z:][::-1]:
                        if I == i:
                            akf[ny2][nx2].append( [i,4,ny2,nx2] )
                        else:
                            akf[ny2][nx2].append([I,D,Y+dy[4],X+dx[4]])

                elif space_color[ny2][nx2] == 2:
                    ny3 = ny2 + dy[3] # <-, '제자리', ->, 다시 '제자리', 방향은 안바꿈
                    nx3 = nx2 + dx[3]
                    for (I,D,Y,X)  in reve[z:]:
                        if I == i:
                            akf[ny3][nx3].append( [i,4,ny3,nx3] )
                        else:
                            akf[ny3][nx3].append([I,D,Y,X])
        elif d == 4:
            ny = y + dy[4]
            nx = x + dx[4] # <-

            if space_color[ny][nx] == 0:
                for (I,D,Y,X) in reve[z:]:
                    akf[ny][nx].append([I,D,Y+dy[4],X+dx[4]])

            elif space_color[ny][nx] == 1:
                for (I,D,Y,X) in reve[z:][::-1]:
                    akf[ny][nx].append([I,D,Y+dy[4],X+dx[4]])

            elif space_color[ny][nx] == 2:
                d = 3 # 벽 붙히져서 다시 원래 재 자리로 이동 // <-, 제자리
                ny = ny + dy[3]
                nx = nx + dx[3]
                ny2 = ny + dy[3] # 제자리에서 다시 움직임. <-, 제자리, ->
                nx2 = nx + dx[3]

                if space_color[ny2][nx2] == 0:
                    for (I,D,Y,X) in reve[z:]:
                        if I == i:
                            akf[ny2][nx2].append( [i,3,ny2,nx2] )
                        else:
                            akf[ny2][nx2].append([I,D,Y+dy[3],X+dx[3]])

                elif space_color[ny2][nx2] == 1:
                    for (I,D,Y,X) in reve[z:][::-1]:
                        if I == i:
                            akf[ny2][nx2].append( [i,3,ny2,nx2] )
                        else:
                            akf[ny2][nx2].append([I,D,Y+dy[3],X+dx[3]])

                elif space_color[ny2][nx2] == 2:
                    ny3 = ny2 + dy[4] # <-, '제자리', ->, 다시 '제자리', 방향은 안바꿈
                    nx3 = nx2 + dx[4]
                    for (I,D,Y,X)  in reve[z:]:
                        if I == i:
                            akf[ny3][nx3].append( [i,3,ny3,nx3] )
                        else:
                            akf[ny3][nx3].append([I,D,Y,X])

        for b in range(1,N+1):
            for a in range(1,N+1):
                if len(akf[b][a]) >= 4:
                    print(turn)
                    exit()

print(-1)
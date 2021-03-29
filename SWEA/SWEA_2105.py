import copy
dy = [1,1,1,-1,-1]
dx = [1,1,-1,-1,1]
def dfs(y,x,length,d, start_y,start_x,change,visit):
    global space
    global result
    # print('y:',y,'x:',x,'length:',length,'d:',d, 'start_y:',start_y,'start_x:',start_x,'change:',change,'visit:',visit)
    # print('---------------')

    if y == start_y and x == start_x and change == 4:
        result.append(length)
        #result.append(visit)
        return True

    if d == 0:
        ny1 = y + dy[0]
        nx1 = x + dx[0]
        change1 = change
        visit1 = copy.deepcopy(visit)
        if 0<= ny1 < N and 0<= nx1 < N and change1 < 5 and space[ny1][nx1] not in visit1:
            visit1.append(space[ny1][nx1])
            dfs(ny1,nx1,length+1, 1, start_y,start_x, change1, visit1)
        

    elif d == 1:
        ny1 = y + dy[1]
        nx1 = x + dx[1]
        change1 = change
        visit1 = copy.deepcopy(visit) # visit1 = visit 하면 안됨!!!!!!!!!!!!!!!!!!!!!!!!!!! 꼭 copy를 이용해야함. 매우 중요
        visit2 = copy.deepcopy(visit)

        if 0<= ny1 < N and 0<= nx1 < N and change1 < 5 and space[ny1][nx1] not in visit1:
            visit1.append(space[ny1][nx1])
            dfs(ny1,nx1,length+1, 1, start_y,start_x, change1, visit1)
        
        ny2 = y + dy[2]
        nx2 = x + dx[2]
        change2 = change + 1
        if 0<= ny2 < N and 0<= nx2 < N and change2 < 5 and space[ny2][nx2] not in visit2:
            visit2.append(space[ny2][nx2])
            dfs(ny2,nx2,length+1, 2, start_y,start_x,change2, visit2)

    elif d == 2:
        ny1 = y + dy[2]
        nx1 = x + dx[2]
        change1 = change
        visit1 = copy.deepcopy(visit)
        visit2 = copy.deepcopy(visit)
        if 0<= ny1 < N and 0<= nx1 < N and change1 < 5 and space[ny1][nx1] not in visit1:
            visit1.append(space[ny1][nx1])
            dfs(ny1,nx1,length+1, 2, start_y,start_x, change1, visit1 ) 

        ny2 = y + dy[3]
        nx2 = x + dx[3]
        change2 = change + 1
        if 0<= ny2 < N and 0<= nx2 < N and change2 < 5 and space[ny2][nx2] not in visit2:
            visit2.append(space[ny2][nx2])
            dfs(ny2,nx2,length+1, 3, start_y,start_x, change2, visit2)

    elif d == 3:
        ny1 = y + dy[3]
        nx1 = x + dx[3]
        change1 = change
        visit1 = copy.deepcopy(visit)
        visit2 = copy.deepcopy(visit)
        if 0<= ny1 < N and 0<= nx1 < N and change1 < 5 and space[ny1][nx1] not in visit1:
            visit1.append(space[ny1][nx1])
            dfs(ny1,nx1,length+1, 3, start_y,start_x, change1, visit1 )

        ny2 = y + dy[4]
        nx2 = x + dx[4]
        change2 = change + 1
        if 0<= ny2 < N and 0<= nx2 < N and change2 < 5 and space[ny2][nx2] not in visit2:
            visit2.append(space[ny2][nx2])
            dfs(ny2,nx2,length+1, 4, start_y,start_x, change2, visit2)

    elif d == 4:
        ny1 = y + dy[4]
        nx1 = x + dx[4]
        change1 = change
        visit1 = copy.deepcopy(visit)
        visit2 = copy.deepcopy(visit)
        if 0<= ny1 < N and 0<= nx1 < N and change1 < 5 and space[ny1][nx1] not in visit1:
            visit1.append(space[ny1][nx1])
            dfs(ny1,nx1,length+1, 4, start_y,start_x, change1, visit1 )

        ny2 = y + dy[1]
        nx2 = x + dx[1]
        change2 = change + 1
        if 0<= ny2 < N and 0<= nx2 < N and change2 < 5 and space[ny2][nx2] not in visit2:
            visit2.append(space[ny2][nx2])
            dfs(ny2,nx2,length+1, 1, start_y,start_x, change2, visit2)


t = int(input())
for tc in range(1,t+1):
    N = int(input())
    space = []
    result = []
    for i in range(N):
        space.append(list(map(int,input().split())))

    for i in range(0, N-2):
        for j in range(1,N-1):
            dfs(i,j,1,0,i,j,1,[])

    if result == []:
        print('#',tc,' ',-1,sep='')
    else:
        print('#',tc,' ',max(result)-1,sep='')
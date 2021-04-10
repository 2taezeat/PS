from collections import deque
# .remove .count 보다는 tmp list 선언 및 할당
R, C, M = map(int,input().split())
space = [[deque() for j in range(C)] for i in range(R)]
shark_loc_list = []
answer = 0
for i in range(M):
    r,c,s,d,z = map(int,input().split())
    space[r-1][c-1].append((s,d,z))
    shark_loc_list.append((r-1,c-1))
dy = [99,-1,1,0,0]
dx = [99,0,0,1,-1]


def move():
    global space
    global shark_loc_list
    tmp = []

    # 각 샤크에 대해
    while (shark_loc_list):
        (y,x) = shark_loc_list.pop()
        sh_info = space[y][x][0]
        speed = sh_info[0]
        dire = sh_info[1]
        size = sh_info[2]
        # 시간복잡도를 위한 속도 트릭
        if dire == 1 or dire == 2:
            speed = speed % (2*R-2)
        elif dire == 3 or dire == 4:
            speed = speed % (2*C-2)

        space[y][x].popleft()      
        S = 0
        while (S < speed):
            if dire == 1:
                ny = y + dy[1]
                nx = x + dx[1]
                if ny < 0:
                    dire = 2
                    ny = ny + dy[2]
                    nx = nx + dx[2]
                    S = S - 1
            elif dire == 2:
                ny = y + dy[2]
                nx = x + dx[2]
                if ny > R - 1:
                    dire = 1
                    ny = ny + dy[1]
                    nx = nx + dx[1]
                    S = S - 1
            elif dire == 3:
                ny = y + dy[3]
                nx = x + dx[3]
                if nx > C-1:
                    dire = 4
                    ny = ny + dy[4]
                    nx = nx + dx[4]
                    S = S - 1
            elif dire == 4:
                ny = y + dy[4]
                nx = x + dx[4]
                if nx < 0:
                    dire = 3
                    ny = ny + dy[3]
                    nx = nx + dx[3]
                    S = S - 1
            y = ny
            x = nx
            S = S + 1
        
        space[y][x].append( (speed,dire,size) )
        tmp.append((y,x))

    return tmp


for peo_loc in range(0,C):
    # 1. 맨위 for문이 낚시왕이 오른쪽으로 한 칸 이동을 의미

    # 2. 가장 가까운 상어 잡고, 상어 없애기
    for capture in range(0,R):
        sh_info = space[capture][peo_loc]
        if sh_info :
            answer = answer + sh_info[0][2]
            space[capture][peo_loc] = deque()
            shark_loc_list.remove((capture,peo_loc))
            break
    

    # 3. 상어 움직임
    shark_loc_list = move()
    # 4. 상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상있을 경우, 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.
    tmp2 = []
    many_shark = []
    for (y,x) in shark_loc_list:
        ls = len(space[y][x]) 
        if ls >= 2:
            many_shark.append((y,x,ls))
        else:
            tmp2.append((y,x))

    many_shark = list(set(many_shark))
    for (y,x,ls) in many_shark:
        tmp2.append((y,x))
        l = space[y][x]
        fight = []
        for J in range(ls):
            fight.append((l[J][2],l[J][1],l[J][0]))

        space[y][x] = deque()
        max_zmrl = max(fight)
        space[y][x].append( ( max_zmrl[2],max_zmrl[1],max_zmrl[0] ) )

    shark_loc_list = tmp2

print(answer)
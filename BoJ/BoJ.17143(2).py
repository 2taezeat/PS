# .remove .count 보다는 tmp list 선언 및 할당
import sys
input = sys.stdin.readline 
R, C, M = map(int,input().split())
space = [[[] for j in range(C)] for i in range(R)]
shark_loc_list = []
answer = 0
for i in range(M):
    r,c,s,d,z = map(int,input().split())
    space[r-1][c-1].append((s,d,z))
    shark_loc_list.append((r-1,c-1))
dy = [99,-1,1,0,0]
dx = [99,0,0,1,-1]
# shark_loc_list 없는 버전

def move(y,x):
    global space
    sh_info = space[y][x][0]
    speed = sh_info[0]
    dire = sh_info[1]
    size = sh_info[2]
    # 시간복잡도를 위한 속도 트릭
    if dire == 1 or dire == 2:
        speed = speed % (2*R-2)
    elif dire == 3 or dire == 4:
        speed = speed % (2*C-2)
    space[y][x] = []   

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
    
    return (y,x,speed,dire,size)

for peo_loc in range(0,C):
    for capture in range(0,R):
        sh_info = space[capture][peo_loc]
        if sh_info :
            answer = answer + sh_info[0][2]
            space[capture][peo_loc] = []
            break
    
    k = []
    for i in range(R):
        for j in range(C):
            if space[i][j] :
                k.append( move(i,j) )
    
    for (y,x,s,d,z) in k:
        space[y][x].append((s,d,z))

    many_shark = []
    for i in range(R):
        for j in range(C):
            if len(space[i][j]) >= 2:
                many_shark.append((i,j,len(space[i][j])))

    for (y,x,ls) in many_shark:
        l = space[y][x]
        fight = []
        for J in range(ls):
            fight.append((l[J][2],l[J][1],l[J][0]))

        space[y][x] = []
        max_zmrl = max(fight)
        space[y][x].append( ( max_zmrl[2],max_zmrl[1],max_zmrl[0] ) )

print(answer)
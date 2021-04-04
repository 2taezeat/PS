import itertools
space = []
for i in range(10):
    space.append(list(map(int,input().split())))
result_list = []
def checking(y,x,qjadnl):
    global space
    for i in range(y,y+qjadnl):
        for j in range(x,x+qjadnl):
            if not (0<= i < 10 and 0<= j < 10):
                return False
            if space[i][j] == 0 or space[i][j] == 7:
                return False
    return True
def paint(y,x,qjadnl):
    global space
    for i in range(y,y+qjadnl):
        for j in range(x,x+qjadnl):
            space[i][j] = 7
def back(y,x,qjadnl):
    global space
    for i in range(y,y+qjadnl):
        for j in range(x,x+qjadnl):
            space[i][j] = 1
def cal(y,x,delta):
    cy = y
    cx = x + delta
    if cx >= 10:
        return y+1,0
    elif (0<= cy < 10 and 0<= cx < 10):
        return cy,cx

def dfs(y,x, p1,p2,p3,p4,p5):
    global space
    global result_list
    
    # 종료 조건 2가지
    if p1 > 5 or p2 > 5 or p3 > 5 or p4 > 5 or p5 > 5:
        return
    if y == 10:
        result_list.append(p1+p2+p3+p4+p5)
        return

    if space[y][x] == 0 or space[y][x] == 7:
        ny,nx = cal(y,x,1)
        dfs(ny,nx, p1,p2,p3,p4,p5)

    else:
        for d in range(5,0,-1):
            if d == 5:
                if checking(y,x,5) == True:
                    paint(y,x,5)
                    ny,nx = cal(y,x,5)
                    dfs(ny,nx, p1,p2,p3,p4,p5+1)
                    back(y,x,5)
            elif d == 4:
                if checking(y,x,4) == True:
                    paint(y,x,4)
                    ny,nx = cal(y,x,4)
                    dfs(ny,nx, p1,p2,p3,p4+1,p5)
                    back(y,x,4)
            elif d == 3:
                if checking(y,x,3) == True:
                    paint(y,x,3)
                    ny,nx = cal(y,x,3)
                    dfs(ny,nx, p1,p2,p3+1,p4,p5)
                    back(y,x,3)
            elif d == 2:
                if checking(y,x,2) == True:
                    paint(y,x,2)
                    ny,nx = cal(y,x,2)
                    dfs(ny,nx, p1,p2+1,p3,p4,p5)
                    back(y,x,2)
            elif d == 1:
                if checking(y,x,1) == True:
                    paint(y,x,1)
                    ny,nx = cal(y,x,1)
                    dfs(ny,nx, p1+1,p2,p3,p4,p5)
                    back(y,x,1)

    return 

dfs(0,0, 0,0,0,0,0)
if result_list == []:
    print(-1)
else:
    print(min(result_list))
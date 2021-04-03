import itertools, copy
space = []
for i in range(10):
    space.append(list(map(int,input().split())))

def check_5(y,x):
    global space
    for Y in range(y,y+5):
        for X in range(x,x+5):
            if not (0<= Y < 10 and 0<= X < 10):
                return False
            else:
                if space[Y][X] != 1:
                    return False
    return True
def check_4(y,x):
    global space
    for Y in range(y,y+4):
        for X in range(x,x+4):
            if not (0<= Y < 10 and 0<= X < 10):
                return False
            else:
                if space[Y][X] != 1:
                    return False
    return True
def check_3(y,x):
    global space
    for Y in range(y,y+3):
        for X in range(x,x+3):
            if not (0<= Y < 10 and 0<= X < 10):
                return False
            else:
                if space[Y][X] != 1:
                    return False
    return True  
def check_2(y,x):
    global space
    for Y in range(y,y+2):
        for X in range(x,x+2):
            if not (0<= Y < 10 and 0<= X < 10):
                return False
            else:
                if space[Y][X] != 1:
                    return False
    return True
def max_cal(y,x):
    global space
    if check_5(y,x):
        return 5
    elif check_4(y,x):
        return 4
    elif check_3(y,x):
        return 3
    elif check_2(y,x):
        return 2
    return 1
for y in range(0,10):
    for x in range(0,10):
        if space[y][x] == 1:
            m_value = max_cal(y,x)
            space[y][x] = m_value

p1,p2,p3,p4,p5 = 0,0,0,0,0

def checking(y,x,qjadnl):
    pass

def paint(y,x,qjadnl):
    pass

def back(y,x,qjadnl):



def dfs(y,x):
    print(y,x)
    if x == 9 and y == 9:
        return


    if space[y][x] == 0:

        if 0<=y < 10 and 0<= x < 10:
            x = x + 1
            y = y
            dfs(y,x)
        elif x == 10:
            x = 0
            y = y + 1
            dfs(y,x)

    else:
        if space[y][x] == 2:
            p2 = p2 + 1
            x = x + 2
            y = y
            dfs(y,x)
        



        

dfs(0,0)
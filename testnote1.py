import itertools, copy
space = []
for i in range(10):
    space.append(list(map(int,input().split())))
space_1 = copy.deepcopy(space)
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
def paint_5(p_space,y,x):
    for Y in range(y,y+5):
        for X in range(x,x+5):
            p_space[Y][X] = 5
def paint_4(p_space,y,x):
    for Y in range(y,y+4):
        for X in range(x,x+4):
            p_space[Y][X] = 4
def paint_3(p_space,y,x):
    for Y in range(y,y+3):
        for X in range(x,x+3):
            p_space[Y][X] = 3
    
    return p_space
def paint_2(p_space,y,x):
    for Y in range(y,y+2):
        for X in range(x,x+2):
            p_space[Y][X] = 2

    return p_space




def dfs(y,x, p1,p2,p3,p4,p5, max_paper, o_space ):

    if max_paper == 5:
        paint_5(o_space,y,x)
    elif max_paper == 4:
        paint_4(o_space,y,x)
    elif max_paper == 3:
        r_space = paint_3(o_space,y,x)

        p3 = p3 + 1
        y = y
        x = x + 3

        mp = space[y][x]
        for m in range(mp,1,-1):
            dfs(y,x,p1,p2,p3,p4,p5, m, r_space)



    elif max_paper == 2:
        r_space = paint_2(o_space,y,x)

        p2 = p2 + 1
        y = y
        x = x + 2
        mp = space[y][x]
        for m in range(mp,1,-1):
            dfs(y,x,p1,p2,p3,p4,p5, m, r_space)


    print('@@@@@@@@')
    for i in range(0,10):
        print(o_space[i])


    




                        
print('---')
for i in range(0,10):
    print(space[i])

dfs(1,1,0,0,0,0,0,2,space_1)

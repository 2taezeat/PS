space = []
l5,l4,l3,l2,l1 = [],[],[],[],[]
paper = [5,5,5,5,5]
for i in range(10):
    space.append(list(map(int,input().split())))
def check_5(y,x):
    global space
    for Y in range(y,y+5):
        for X in range(x,x+5):
            try:
                if space[Y][X] != 1:
                    return False
            except:
                pass
    return True

def check_4(y,x):
    global space
    for Y in range(y,y+4):
        for X in range(x,x+4):
            try:
                if space[Y][X] != 1:
                    return False
            except:
                pass
    return True

def check_3(y,x):
    global space
    for Y in range(y,y+3):
        for X in range(x,x+3):
            try:
                if space[Y][X] != 1:
                    return False
            except:
                pass
    return True
    
def check_2(y,x):
    global space
    for Y in range(y,y+2):
        for X in range(x,x+2):
            try:
                if space[Y][X] != 1:
                    return False
            except:
                pass
    return True

def max_cal(y,x):
    global space
    if check_5(y,x):
        return 5
    elif check_4(y,x):
        return 4
    elif check_4(y,x):
        return 3
    elif check_4(y,x):
        return 2
    return 1



for y in range(0,10):
    for x in range(0,10):
        if space[y][x] == 1:
            m_value = max_cal(y,x)
            space[y][x] = m_value

                        
print('---')
for i in range(0,10):
    print(space[i])
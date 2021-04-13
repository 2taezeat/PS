N = int(input())
space = [[0]*10 for i in range(10)]
answer = 0
dy = [0,1]
dx = [1,0]
def move_right(t,y,x):
    global space
    if t == 1:
        for j in range(x,9):
            ny1 = y + dy[0]
            nx1 = x + dx[0]
            if space[ny1][nx1] == 1:
                space[y][x] = 1
                break
            elif nx1 == 9:
                space[ny1][nx1] = 1

            y = ny1
            x = nx1
                
    elif t == 2:
        y = y 
        x = x + 1
        for j in range(x,9):
            ny2 = y + dy[0]
            nx2 = x + dx[0]
            if space[ny2][nx2] == 1:
                space[ny2][nx2-2] = 1
                space[ny2][nx2-1] = 1
                break
            elif nx2 == 9:
                space[ny2][nx2] = 1
                space[ny2][nx2-1] = 1

            y = ny2
            x = nx2

    elif t == 3:
        y1 = y
        x1 = x 

        y2 = (y+1)
        x2 = x
        for j in range(x,9):
            ny1 = y1 + dy[0]
            nx1 = x1 + dx[0]

            ny2 = y2 + dy[0]
            nx2 = x2 + dx[0]
            if space[ny1][nx1] == 1 or space[ny2][nx2] == 1:
                space[y1][x1] = 1
                space[y2][x2] = 1
                break
        
            elif nx1 == 9 or nx2 == 9:
                space[ny1][nx1] = 1
                space[ny2][nx2] = 1
            y1 = ny1
            x1 = nx1
            y2 = ny2
            x2 = nx2

def move_down(t,y,x):
    global space
    if t == 1:
        for _ in range(y,9):
            ny1 = y + dy[1]
            nx1 = x + dx[1]
            if space[ny1][nx1] == 1:
                space[y][x] = 1
                break
            elif ny1 == 9:
                space[ny1][nx1] = 1
            y = ny1
            x = nx1
                
    elif t == 2:
        y1 = y
        x1 = x 

        y2 = y
        x2 = (x+1)
        for _ in range(y,9):
            ny1 = y1 + dy[1]
            nx1 = x1 + dx[1]

            ny2 = y2 + dy[1]
            nx2 = x2 + dx[1]
            if space[ny1][nx1] == 1 or space[ny2][nx2] == 1:
                space[y1][x1] = 1
                space[y2][x2] = 1
                break
            
            elif ny1 == 9 or ny2 == 9:
                space[ny1][nx1] = 1
                space[ny2][nx2] = 1
            y1 = ny1
            x1 = nx1
            y2 = ny2
            x2 = nx2

    elif t == 3:
        y = y + 1
        x = x
        for _ in range(y,9):
            ny2 = y + dy[1]
            nx2 = x + dx[1]
            if space[ny2][nx2] == 1:
                space[ny2-1][nx2] = 1
                space[ny2-2][nx2] = 1
                break
            elif ny2 == 9:
                space[ny2-1][nx2] = 1
                space[ny2][nx2] = 1
            y = ny2
            x = nx2

def right_score():
    global answer
    for j in range(4,10):
        count = 0
        for i in range(0,4):
            if space[i][j] == 1:
                count +=1
            else:
                break
        if count == 4:
            answer += 1
            
            for J in range(j,4,-1):
                for I in range(0,4):
                    space[I][J] = space[I][J-1]
            
            space[0][4] = 0
            space[1][4] = 0
            space[2][4] = 0
            space[3][4] = 0

def down_score():
    global answer
    for i in range(4,10):
        count = 0
        for j in range(0,4):
            if space[i][j] == 1:
                count +=1
            else:
                break
        if count == 4:
            answer += 1
            
            for I in range(i,4,-1):
                for J in range(0,4):
                    space[I][J] = space[I-1][J]
            
            space[4][0] = 0
            space[4][1] = 0
            space[4][2] = 0
            space[4][3] = 0

def dusgks_green():
    global space
    real_count = 0
    for i in range(4,6):
        count = 0
        for j in range(0,4):
            if space[i][j] == 1:
                count += 1
                break

        if count >= 1:
            real_count += 1

    for _ in range(real_count):

        for I in range(9,4,-1):
            for J in range(0,4):
                space[I][J] = space[I-1][J]
                
        space[4][0] = 0
        space[4][1] = 0
        space[4][2] = 0
        space[4][3] = 0

def dusgks_blue():
    global space
    real_count = 0
    for j in range(4,6):
        count = 0
        for i in range(0,4):
            if space[i][j] == 1:
                count += 1
                break

        if count >= 1:
            real_count += 1

    for _ in range(real_count):

        for J in range(9,4,-1):
            for I in range(0,4):
                space[I][J] = space[I][J-1]
                
        space[0][4] = 0
        space[1][4] = 0
        space[2][4] = 0
        space[3][4] = 0

for i in range(N):
    t, x, y = map(int,input().split())
    b = x
    a = y

    move_right(t,b,a)
    move_down(t,b,a)

    right_score()
    down_score()

    dusgks_green()
    dusgks_blue()


blue = 0
green = 0
for i in range(0,4):
    for j in range(4,10):
        if space[i][j] == 1:
            blue += 1
for i in range(4,10):
    for j in range(0,4):
        if space[i][j] == 1:
            green += 1
print(answer)
print(green + blue)

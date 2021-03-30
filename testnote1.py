import itertools, copy
N,M,H = map(int,input().split())
space = [[0]*N for i in range(H)]
h_list = []
for i in range(M):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    space[a][b] = 1
    space[a][b+1] = 1
for i in range(H):
    h = []
    for j in range(N-1):
        if j == 0:
            if space[i][j] == 0 and space[i][1] == 0:
                h.append((0,1,i))
        elif j == N-2:
            if space[i][j] == 0 and space[i][j+1] == 0:
                h.append((j,j+1,i))
        else:
            if space[i][j] == 0 and space[i][j+1] == 0 :
                h.append((j,j+1,i))
    
    h_list.append(h)

def fall(space, frist_x):
    global result_list
    x = frist_x
    for i in range(H):
        if space[i][x] == 1:
            x = x + 1
        elif space[i][x] == 2 :
            x = x - 1

        # if x == 0:
        #     if space[i][0]== 1:
        #         x = x + 1

        # elif x == N-1:
        #     if space[i][N-1] == 1:
        #         x = x - 1

        # elif x == 1:
        #     if space[i][x] == 1:
        #         x = x + 1
        #     elif space[i][x] == 2 :
        #         x = x - 1
    
        # elif x == N-1-1:
        #     if space[i][x] == 1:
        #         x = x + 1
                    
        #     elif space[i][x] == 2 :
        #         x = x - 1

        # else:
        #     if space[i][x] == 1:
        #         x = x + 1
        #     elif space[i][x] == 2:
        #         x = x - 1

        print(x)

    if x == frist_x:
        result_list.append(x)
        return True
    else:
        result_list.append(x)
        return False

result_list = []
# space = [[1, 1, 0, 0, 0],[0, 0, 1, 1, 0],[0, 1, 1, 0, 0],[0, 0, 0, 1, 1],[1, 1, 0, 1, 1],[0, 1, 1, 1, 1]]
space = [[1, 2, 1, 2, 1, 2],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 1, 2, 1, 2, 0],
[0, 0, 0, 0, 0, 0]]

for i in range(N):
    print(fall(space,i))
    print('-----------')

print(result_list)
N, M , x, y, K = map(int,input().split())
space = []
for i in range(N):
    space.append(list(map(int,input().split())))
order = list(map(int,input().split()))
dice = [0,0,0,0,0,0]

for i in range(K):
    D = order[i]

    if D == 1:
        dx = x
        dy = y + 1
    elif D == 2:
        dx = x
        dy = y - 1 
    elif D == 3:
        dx = x - 1
        dy = y
    elif D == 4:
        dx = x + 1 
        dy = y

    if (0 <= dx < N and 0 <= dy < M):
        # 주사위 회전
        if D == 1:
            dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[3],dice[1],dice[0],dice[5],dice[4],dice[2] 
        elif D == 2:
            dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[2],dice[1],dice[5],dice[0],dice[4],dice[3] 
        elif D == 3:
            dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[4],dice[0],dice[2],dice[3],dice[5],dice[1] 
        elif D == 4:
            dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]

        if space[dx][dy] == 0:
            # 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
            space[dx][dy] = dice[5]

        else:
            dice[5] = space[dx][dy]
            space[dx][dy] = 0
        
        print(dice[0])

        x = dx
        y = dy
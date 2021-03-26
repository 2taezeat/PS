import copy
N, L = map(int,input().split())
o_space = []
for i in range(N):
    list1 = list(map(int,input().split()))
    l2 = []
    for l in list1:
        l2.append([l,100])
    o_space.append(l2)
answer1 = []
answer2 = []
t_space = list(zip(*o_space)) # 2차원안에 또 다른 배열이 있어서 예상하는거랑 다르게 변환되는듯 

# 가로 확인
for i in range(N):
    judge = True
    k = 0
    while(k < N-1):
        if o_space[i][k+1][0] - o_space[i][k][0] == 1:
            for l in range(L):
                if (0 <= k-l) and o_space[i][k-l][1] == 100 :
                    o_space[i][k-l][1] = 200
                else:
                    judge = False
                    break
            k = k + 1

        elif o_space[i][k+1][0] - o_space[i][k][0] == -1:
            for l in range(L):
                if (k+l+1 < N) and o_space[i][k+l+1][1] == 100 :
                    o_space[i][k+l+1][1] = 300
                else:
                    judge = False
                    break
            k = k + 1

        elif o_space[i][k+1][0] - o_space[i][k][0] > 1 or o_space[i][k+1][0] - o_space[i][k][0] < -1 :
            judge = False
            break

        else:
            k = k + 1

    if judge:
        answer1.append(i)

# trans배열 다시 초기화
for i in range(N):
    for j in range(N):
        t_space[i][j][1] = 100


# 세로 확인
for i in range(N):
    judge2 = True
    k = 0
    while(k < N-1):
        if t_space[i][k+1][0] - t_space[i][k][0] == 1:
            for l in range(L):
                if (0 <= k-l) and t_space[i][k-l][1] == 100 :
                    t_space[i][k-l][1] = 200
                else:
                    judge2 = False
                    break
            k = k + 1

        elif t_space[i][k+1][0] - t_space[i][k][0] == -1:
            for l in range(L):
                if (k+l+1 < N) and t_space[i][k+l+1][1] == 100 :
                    t_space[i][k+l+1][1] = 300
                else:
                    judge2 = False
                    break
            k = k + 1

        elif t_space[i][k+1][0] - t_space[i][k][0] > 1 or t_space[i][k+1][0] - t_space[i][k][0] < -1 :
            judge2 = False
            break

        else:
            k = k + 1

    if judge2:
        answer2.append(i)

print(len(answer1)+len(answer2))
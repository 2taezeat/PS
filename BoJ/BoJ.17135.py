import copy
N, M, D = map(int,input().split())
space = []
for i in range(N):
    space.append(list(map(int,input().split())))
a = [0 for _ in range(M)]
space.append(a)
result = []
    
for i in range(M):
    for j in range(i+1,M):
        for k in range(j+1,M):
            eli_count = 0
            gameover_check = 1
            n_space = copy.deepcopy(space)
            n_space[N][i] = 9
            n_space[N][j] = 9
            n_space[N][k] = 9
########################### attack

            for r in range(N):
                q = 1
                l1,l2,l3 = [],[],[]
                for Y in range(0,N):
                    for X in range(0,M):
                        if n_space[Y][X] == 1:
                            distance1 = abs(Y-N) + abs(X-i)
                            distance2 = abs(Y-N) + abs(X-j)
                            distance3 = abs(Y-N) + abs(X-k)

                            if distance1 <= D:
                                l1.append((distance1,Y,X))
                            if distance2 <= D:
                                l2.append((distance2,Y,X))
                            if distance3 <= D:
                                l3.append((distance3,Y,X))

                l1.sort(key= lambda x: (x[0],x[2]))
                l2.sort(key= lambda x: (x[0],x[2]))
                l3.sort(key= lambda x: (x[0],x[2]))
                if l1 != []:
                    if n_space[l1[0][1]][l1[0][2]] == 1:
                        n_space[l1[0][1]][l1[0][2]] = 0
                        eli_count += 1
                if l2 != []:
                    if n_space[l2[0][1]][l2[0][2]] == 1:
                        n_space[l2[0][1]][l2[0][2]] = 0
                        eli_count += 1
                if l3 != []:
                    if n_space[l3[0][1]][l3[0][2]] == 1:
                        n_space[l3[0][1]][l3[0][2]] = 0
                        eli_count += 1

########################### fall
                for y in range(N-2,-1,-1):
                    for x in range(0,M):
                        if n_space[y][x] == 1:
                            gameover_check = 0

                        n_space[y+1][x] = n_space[y][x]

                for a in range(M):
                    n_space[0][a] = 0

    ########################## gameover check
                if gameover_check == 1:
                    result.append(eli_count)
                    q = 0
                    break
            #     print(eli_count)
            #     for t in range(N):
            #         print(n_space[t])
            #     print('@@@@@@@@@@@@@')

            # print('---------------')
            # print(i,j,k)

            if q == 1:
                result.append(eli_count)


        #print('---------------')


print(max(result))
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

            if i == 0 and j == 2 and k == 4:

                for r in range(N):
                    q = 1
                    l1,l2,l3 = [],[],[]
                    for y in range(0,N):
                        for x in range(0,M):
                            if n_space[y][x] == 1:
                                distance1 = abs(y-N) + abs(x-i)
                                distance2 = abs(y-N) + abs(x-j)
                                distance3 = abs(y-N) + abs(x-k)
                                #print(r,distance1,y,x,N,i)
                                if distance1 <= D:
                                    l1.append((distance1,y,x))
                                if distance2 <= D:
                                    l2.append((distance2,y,x))
                                if distance3 <= D:
                                    l3.append((distance3,y,x))

                    l1.sort(key= lambda x: (x[0],x[2]))
                    l2.sort(key= lambda x: (x[0],x[2]))
                    l3.sort(key= lambda x: (x[0],x[2]))
                    print(l1,l2,l3)
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
                    print(eli_count)

                    for i in range(N):
                        print(n_space[i])
                    print('---------------')

                if q == 1:
                    result.append(eli_count)





print(max(result))
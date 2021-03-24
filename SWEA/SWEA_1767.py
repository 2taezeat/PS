from itertools import product
import copy
tc = int(input())
for t in range(tc):
    o_space = []
    n = int(input())
    for i in range(n):
        o_space.append(list(map(int,input().split())))

    case = []
    for i in range(1,n-1):
        for j in range(1,n-1):
            if o_space[i][j] == 1:
                dlist = [1,2,3,4]

                for k in range(i-1,-1,-1):
                    if o_space[k][j] == 1:
                        dlist.remove(1)
                        break

                for k in range(i+1,n,+1):
                    if o_space[k][j] == 1:
                        dlist.remove(2)
                        break

                for k in range(j-1,-1,-1):
                    if o_space[i][k] == 1:
                        dlist.remove(3)
                        break

                for k in range(j+1,n,+1):
                    if o_space[i][k] == 1:
                        dlist.remove(4)
                        break
                subcase = []
                for d in dlist:
                    subcase.append((i,j,d))
                if subcase != []:
                    case.append(subcase)
    #print(case)
    pl = list(product(*case))
    answer = []
    #print(pl)
    for p in pl:
        n_space = copy.deepcopy(o_space)
        final_line = 0
        c_len = len(case)
        for loc in p:
            subline = 0
            x, y = loc[1], loc[0]

            if loc[2] == 1:
                for k in range(y-1,-1,-1):
                    if n_space[k][x] == 0:
                        n_space[k][x] = 1
                        subline += 1
                
                    else:
                        subline = 0
                        c_len -= 1
                        break

            elif loc[2] == 2:
                for k in range(y+1,n,+1):
                    if n_space[k][x] == 0:
                        n_space[k][x] = 1
                        subline += 1
                
                    else:
                        subline = 0
                        c_len -= 1
                        break

            elif loc[2] == 3:
                for k in range(x-1,-1,-1):
                    if n_space[y][k] == 0:
                        n_space[y][k] = 1
                        subline += 1
                
                    else:
                        subline = 0
                        c_len -= 1
                        break

            elif loc[2] == 4:
                for k in range(x+1,n,+1):
                    if n_space[y][k] == 0:
                        n_space[y][k] = 1
                        subline += 1
                
                    else:
                        subline = 0
                        c_len -= 1
                        break

            final_line = final_line + subline

        answer.append([c_len, final_line])
    

    answer.sort()
    f = sorted(answer, key = lambda x : (-x[0], x[1]))
    # print(f)
    print("#",t+1,' ',f[0][1], sep='')
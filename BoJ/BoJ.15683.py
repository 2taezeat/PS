import copy
import itertools
N , M = map(int,input().split())
l1,l2,l3,l4,l5,space,r1,r2,r3,r4,r5 = [],[],[],[],[],[],[],[],[],[],[]
for i in range(N):
    a = list(map(int,input().split()))
    space.append(a)
    for j in range(M):
        s1,s2,s3,s4,s5 = [],[],[],[],[]
        if a[j] == 1:
            l1.append([i,j])
            s1.append([i,j,'w',-1])
            s1.append([i,j,'s',-1])
            s1.append([i,j,'e',-1])
            s1.append([i,j,'n',-1])

        if a[j] == 2:
            l2.append([i,j])
            s2.append([i,j,'e',-2])
            s2.append([i,j,'n',-2])

        if a[j] == 3:
            l3.append([i,j])
            s3.append([i,j,'w',-3])
            s3.append([i,j,'s',-3])
            s3.append([i,j,'e',-3])
            s3.append([i,j,'n',-3])

        if a[j] == 4:
            l4.append([i,j])
            s4.append([i,j,'w',-4])
            s4.append([i,j,'s',-4])
            s4.append([i,j,'e',-4])
            s4.append([i,j,'n',-4])

        if a[j] == 5:
            l5.append([i,j])
            s5.append([i,j,'n',-5])

        if s1 != []:
            r1.append(s1)
        if s2 != []:
            r2.append(s2)
        if s3 != []:
            r3.append(s3)
        if s4 != []:
            r4.append(s4)
        if s5 != []:
            r5.append(s5)
r0 = r1 + r2 + r3 + r4 + r5
p0 = list(itertools.product(*r0))
answer = 1000000
for p in p0:
    nspace = copy.deepcopy(space)
    result = 0
    for case in p:
        if case[3] == -1:
            y1,x1 = case[0], case[1]
            fy1, fx1 = y1, x1
        
            if case[2] == 'w':
                while (0<=x1<M):
                    if nspace[y1][x1] == 6:
                        break
                    y1 = y1
                    x1 = x1 - 1
                    if (0<=x1<M) and nspace[y1][x1] == 0 :
                        nspace[y1][x1] = 1
            
            if case[2] == 's':
                while (0<=y1<N):
                    if nspace[y1][x1] == 6:
                        break
                    y1 = y1 + 1
                    x1 = x1
                    if (0<=y1<N) and nspace[y1][x1] == 0:
                        nspace[y1][x1] = 1
            
            if case[2] == 'e':
                while (0<=x1<M):
                    if nspace[y1][x1] == 6:
                        break
                    y1 = y1
                    x1 = x1 + 1
                    if (0<=x1<M) and nspace[y1][x1] == 0 :
                        nspace[y1][x1] = 1
            
            if case[2] == 'n':
                while (0<=y1<N):
                    if nspace[y1][x1] == 6:
                        break
                    y1 = y1 - 1
                    x1 = x1
                    if (0<=y1<N) and nspace[y1][x1] == 0:
                        nspace[y1][x1] = 1

        if case[3] == -2:
            y2,x2 = case[0], case[1]
            fy2, fx2 = y2, x2

            if case[2] == 'n':
                while (0<=y2<N):
                    if nspace[y2][x2] == 6:
                        break
                    y2 = y2 - 1
                    x2 = x2
                    if (0<=y2<N) and nspace[y2][x2] == 0:
                        nspace[y2][x2] = 2

                y2, x2 = fy2, fx2
                while (0<=y2<N):
                    if nspace[y2][x2] == 6:
                        break
                    y2 = y2 + 1
                    x2 = x2
                    if (0<=y2<N) and nspace[y2][x2] == 0:
                        nspace[y2][x2] = 2

            if case[2] == 'e':
                while (0<=x2<M):
                    if nspace[y2][x2] == 6:
                        break
                    y2 = y2
                    x2 = x2 - 1
                    if (0<=x2<M) and nspace[y2][x2] == 0 :
                        nspace[y2][x2] = 2

                y2, x2 = fy2, fx2
                while (0<=x2<M):
                    if nspace[y2][x2] == 6:
                        break
                    y2 = y2
                    x2 = x2 + 1
                    if (0<=x2<M) and nspace[y2][x2] == 0 :
                        nspace[y2][x2] = 2
            
        if case[3] == -3:
            y3,x3 = case[0], case[1]
            fy3, fx3 = y3, x3

            if case[2] == 'w':
                while (0<=x3<M):
                    if nspace[y3][x3] == 6:
                        break
                    y3 = y3
                    x3 = x3 - 1
                    if (0<=x3<M) and nspace[y3][x3] == 0 :
                        nspace[y3][x3] = 3

                y3, x3 = fy3, fx3

                while (0<=y3<N):
                    if nspace[y3][x3] == 6:
                        break
                    y3 = y3 - 1
                    x3 = x3
                    if (0<=y3<N) and nspace[y3][x3] == 0 :
                        nspace[y3][x3] = 3
                
            if case[2] == 'e':
                while (0<=x3<M):
                    if nspace[y3][x3] == 6:
                        break
                    y3 = y3
                    x3 = x3 + 1
                    if (0<=x3<M) and nspace[y3][x3] == 0 :
                        nspace[y3][x3] = 3
                y3, x3 = fy3, fx3
                  
                while (0<=y3<N):
                    if nspace[y3][x3] == 6:
                        break
                    y3 = y3 - 1
                    x3 = x3
                    if (0<=y3<N) and nspace[y3][x3] == 0 :
                        nspace[y3][x3] = 3

            if case[2] == 'n':
                while (0<=x3<M):
                    if nspace[y3][x3] == 6:
                        break
                    y3 = y3
                    x3 = x3 + 1
                    if (0<=x3<M) and nspace[y3][x3] == 0 :
                        nspace[y3][x3] = 3

                y3, x3 = fy3, fx3
                  
                while (0<=y3<N):
                    if nspace[y3][x3] == 6:
                        break
                    y3 = y3 + 1
                    x3 = x3
                    if (0<=y3<N) and nspace[y3][x3] == 0 :
                        nspace[y3][x3] = 3

            
            if case[2] == 's':
                while (0<=x3<M):
                    if nspace[y3][x3] == 6:
                        break
                    y3 = y3
                    x3 = x3 - 1
                    if (0<=x3<M) and nspace[y3][x3] == 0 :
                        nspace[y3][x3] = 3

                y3, x3 = fy3, fx3
                  
                while (0<=y3<N):
                    if nspace[y3][x3] == 6:
                        break
                    y3 = y3 + 1
                    x3 = x3
                    if (0<=y3<N) and nspace[y3][x3] == 0 :
                        nspace[y3][x3] = 3

        if case[3] == -4:
            y4,x4 = case[0], case[1]
            fy4, fx4 = y4, x4

            if case[2] == 'w':
                while (0<=x4<M):
                    if nspace[y4][x4] == 6:
                        break
                    y4 = y4
                    x4 = x4 - 1
                    if (0<=x4<M) and nspace[y4][x4] == 0 :
                        nspace[y4][x4] = 4
                    
                y4, x4 = fy4, fx4  
                while (0<=y4<N):
                    if nspace[y4][x4] == 6:
                        break
                    y4 = y4 - 1
                    x4 = x4
                    if (0<=y4<N) and nspace[y4][x4] == 0 :
                        nspace[y4][x4] = 4
                    
                y4, x4 = fy4, fx4
                while (0<=y4<N):
                    if nspace[y4][x4] == 6:
                        break
                    y4 = y4 + 1
                    x4 = x4
                    if (0<=y4<N) and nspace[y4][x4] == 0 :
                        nspace[y4][x4] = 4

                    
            if case[2] == 'e':
                while (0<=x4<M):
                    if nspace[y4][x4] == 6:
                        break
                    y4 = y4
                    x4 = x4 + 1
                    if (0<=x4<M) and nspace[y4][x4] == 0 :
                        nspace[y4][x4] = 4

                y4, x4 = fy4, fx4  
                while (0<=y4<N):
                    if nspace[y4][x4] == 6:
                        break
                    y4 = y4 - 1
                    x4 = x4
                    if (0<=y4<N) and nspace[y4][x4] == 0 :
                        nspace[y4][x4] = 4

                y4, x4 = fy4, fx4
                while (0<=y4<N):
                    if nspace[y4][x4] == 6:
                        break
                    y4 = y4 + 1
                    x4 = x4
                    if (0<=y4<N) and nspace[y4][x4] == 0 :
                        nspace[y4][x4] = 4

            if case[2] == 'n':
                while (0<=x4<M):
                    if nspace[y4][x4] == 6:
                        break
                    y4 = y4
                    x4 = x4 + 1
                    if (0<=x4<M) and nspace[y4][x4] == 0 :
                        nspace[y4][x4] = 4

                y4, x4 = fy4, fx4  
                while (0<=x4<M):
                    if nspace[y4][x4] == 6:
                        break
                    y4 = y4
                    x4 = x4 - 1
                    if (0<=x4<M) and nspace[y4][x4] == 0 :
                        nspace[y4][x4] = 4

                    
                y4, x4 = fy4, fx4
                while (0<=y4<N):
                    if nspace[y4][x4] == 6:
                        break
                    y4 = y4 - 1
                    x4 = x4
                    if (0<=y4<N) and nspace[y4][x4] == 0 :
                        nspace[y4][x4] = 4

            if case[2] == 's':
                while (0<=x4<M):
                    if nspace[y4][x4] == 6:
                        break
                    y4 = y4
                    x4 = x4 + 1
                    if (0<=x4<M) and nspace[y4][x4] == 0 :
                        nspace[y4][x4] = 4
                    
                y4, x4 = fy4, fx4  
                while (0<=x4<M):
                    if nspace[y4][x4] == 6:
                        break
                    y4 = y4
                    x4 = x4 - 1
                    if (0<=x4<M) and nspace[y4][x4] == 0 :
                        nspace[y4][x4] = 4
                    
                y4, x4 = fy4, fx4
                while (0<=y4<N):
                    if nspace[y4][x4] == 6:
                        break
                    y4 = y4 + 1
                    x4 = x4
                    if (0<=y4<N) and nspace[y4][x4] == 0 :
                        nspace[y4][x4] = 4

        if case[3] == -5:
            y,x = case[0], case[1]
            fy, fx = y, x
            while (0<=x<M):
                if nspace[y][x] == 6:
                    break
                y = y
                x = x - 1
                if (0<=x<M) and nspace[y][x] == 0 :
                    nspace[y][x] = 5

            y, x = fy, fx  
            while (0<=x<M):
                if nspace[y][x] == 6:
                    break
                y = y
                x = x + 1
                if (0<=x<M) and nspace[y][x] == 0:
                    nspace[y][x] = 5

            y, x = fy, fx
            while (0<=y<N):
                if nspace[y][x] == 6:
                    break
                y = y + 1
                x = x
                if (0<=y<N) and nspace[y][x] == 0:
                    nspace[y][x] = 5

            y, x = fy, fx
            while (0<=y<N):
                if nspace[y][x] == 6:
                    break
                y = y - 1
                x = x
                if (0<=y<N) and nspace[y][x] == 0:
                    nspace[y][x] = 5

    for y in range(N):
        for x in range(M):
            if nspace[y][x] == 0:
                result += 1

    answer = min(answer, result)

print(answer)
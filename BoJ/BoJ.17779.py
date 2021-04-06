import copy
N = int(input())
peo,gnqh,result = [],[],[]
for i in range(N):
    peo.append( list(map(int,input().split())))
o_space = [ [ 0 for j in range(N)] for i in range(N)]

def separte(y,x,d1,d2,space):
    i,j = y,x
    while(1):
        if j > x + d2 or i > N -1:
            break
        space[i][j] = 9
        i = i + 1
        j = j + 1

    i,j = y,x
    while(1):
        if j < x - d1 or i > N -1:
            break
        space[i][j] = 9
        j = j - 1
        i = i + 1

    i,j = y + d1, x - d1
    while(1):
        if i > d1 + d2 + y or j > N - 1:
            break
        space[i][j] = 9
        j = j + 1
        i = i + 1

    i,j = y + d2, x + d2
    while(1):
        if i > y + d1 + d2 or j < 0:
            break
        space[i][j] = 9
        j = j - 1
        i = i + 1

    return space
    
# 후보 만들기
for b in range(0,N-2):
    for a in range(1, N-1):
        for D1 in range(1,N-1):
            for D2 in range(1,N-1):
                c1 = a + D2
                c2 = a - D2
                c3 = b + D1 + D2

                if 0<= c1 < N and 0<= c2 < N and 0<= c3 < N:
                    gnqh.append((b,a,D1,D2))

for Y,X,D1,D2 in gnqh:
    n_space = copy.deepcopy(o_space)
    n_space = separte(Y,X,D1,D2,n_space)
    l1,l2,l3,l4,l5 = [],[],[],[],[]

    for i in range(N):
        q = 0
        lll = []
        for j in range(N):
            if Y <= i <= Y + D1 + D2:
                if n_space[i][j] == 9:
                    lll.append(j)
                    q = q + 1
                if q == 2:
                    for k in range(lll[0]+1,lll[1]):
                        n_space[i][k] = 9
                    q = 0

    for i in range(N):
        for j in range(N):
            if n_space[i][j] == 9:
                l5.append((i,j))
            else:
                if 0 <= j <= X and 0<= i < Y + D1 :
                    n_space[i][j] = 1
                    l1.append((i,j))

                elif X < j < N and 0<= i <= Y + D2 :
                    n_space[i][j] = 2
                    l2.append((i,j))

                elif 0 <= j < X-D1+D2 and Y + D1 <= i < N :
                    n_space[i][j] = 3
                    l3.append((i,j))

                elif X-D1+D2 <= j < N and Y + D2 <= i < N :
                    n_space[i][j] = 4
                    l4.append((i,j))
    
    sum1, sum2, sum3, sum4, sum5 = 0,0,0,0,0
    for I,J in l1:
        sum1 = sum1 + peo[I][J]
    for I,J in l2:
        sum2 = sum2 + peo[I][J]
    for I,J in l3:
        sum3 = sum3 + peo[I][J]
    for I,J in l4:
        sum4 = sum4 + peo[I][J]
    for I,J in l5:
        sum5 = sum5 + peo[I][J]

    mx = max(sum1,sum2,sum3,sum4,sum5)
    mi = min(sum1,sum2,sum3,sum4,sum5)
    result.append(abs(mx-mi))

print(min(result))
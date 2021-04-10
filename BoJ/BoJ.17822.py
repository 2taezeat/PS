from collections import deque
import copy
N, M, T = map(int,input().split())
space = [deque([0])*M for i in range(N+1)]
dlqfur = []
for i in range(N):
    dlqfur.append( list(map(int,input().split())) )
for i in range(N):
    for j in range(M):
        space[ i+1 ] [ j ] = dlqfur[i][j]

for i in range(T):
    x, d, k = map(int,input().split())
    dnjsvks_x = []
    u = 1
    while(1):
        if x*u > N:
            break
        dnjsvks_x.append(x*u)
        u = u + 1

    for j in dnjsvks_x:
        if d == 0:
            for _ in range(k):
                a = space[j].pop()
                space[j].appendleft(a)

        elif d == 1:
            for _ in range(k):
                a = space[j].popleft()
                space[j].append(a)

    before = copy.deepcopy(space)
    tmp = [deque([0])*M for i in range(N+1)]

    for b in range(1,N+1):
        for a in range(0,M):
            if space[b][a] == 'x':
                tmp[b][a] = 'x'
                continue
            standard = space[b][a]
            tmp[b][a] = standard

            if b == 1:
                if space[b][(a-1)%M] == standard :
                    tmp[b][a] = 'x'
                if space[b][(a+1)%M] == standard :
                    tmp[b][a] = 'x'
                if space[(b+1)%(N+1)][a] == standard :
                    tmp[b][a] = 'x'

            elif b == N:
                if space[b][(a-1)%M] == standard :
                    tmp[b][a] = 'x'
                if space[b][(a+1)%M] == standard :
                    tmp[b][a] = 'x'
                if space[(b-1)%(N+1)][a] == standard :
                    tmp[b][a] = 'x'

            else:
                if space[b][(a-1)%M] == standard :
                    tmp[b][a] = 'x'
                if space[b][(a+1)%M] == standard :
                    tmp[b][a] = 'x'
                if space[(b-1)%(N+1)][a] == standard :
                    tmp[b][a] = 'x'
                if space[(b+1)%(N+1)][a] == standard :
                    tmp[b][a] = 'x'

    space = copy.deepcopy(tmp)

    average = 0
    if before == space:
        sum1 = 0
        div = 0
        for b in range(1,N+1):
            for a in range(0,M):
                ele = space[b][a]
                if ele != 'x':
                    sum1 = sum1 + ele
                    div = div + 1
        if div == 0: # diveidezero error 방지용
            average = 0
        else:
            average = sum1 / (div)
        for b in range(1,N+1):
            for a in range(0,M):
                value = space[b][a]
                if value != 'x':
                    if average > value:
                        space[b][a] += 1
                    elif average < value:
                        space[b][a] -= 1
        
answer = 0
for b in range(1,N+1):
    for a in range(0,M):
        ele = space[b][a]
        if ele != 'x':
            answer  = answer  + ele

print(answer)
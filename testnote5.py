from collections import deque
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

    
    count = 0
    for b in range(1,N+1):
        for a in range(0,M):
            if space[b][a] == 'x':
                continue
            standard = space[b][a]

            if b == 1:
                if space[b][(a-1)%M] == standard :
                    space[b][(a-1)%M] = 'x'
                    space[b][a] = 'x'
                    count += 1
                if space[b][(a+1)%M] == standard :
                    space[b][(a+1)%M] = 'x'
                    space[b][a] = 'x'
                    count += 1
                if space[(b+1)%M][a] == standard :
                    space[(b+1%M)][a] = 'x'
                    space[b][a] = 'x'
                    count += 1

            elif b == N:
                if space[b][(a-1)%M] == standard :
                    space[b][(a-1)%M] = 'x'
                    space[b][a] ='x'
                    count += 1
                if space[b][(a+1)%M] == standard :
                    space[b][(a+1)%M] = 'x'
                    space[b][a] ='x'
                    count += 1
                if space[(b-1)%M][a] == standard :
                    space[(b-1)%M][a] = 'x'
                    space[b][a] = 'x'
                    count += 1

            else:
                print(b,a,space[b][a], space[b][(a-1)%M])
                if space[b][(a-1)%M] == standard :
                    print(space[b][a])

                    space[b][(a-1)%M] = 'x'
                    space[b][a] = 'x'
                    count += 1
                if space[b][(a+1)%M] == standard :
                    space[b][(a+1)%M] = 'x'
                    space[b][a] = 'x'
                    count += 1
                if space[(b-1)%M][a] == standard :
                    space[(b-1)%M][a] = 'x'
                    space[b][a] = 'x'
                    count += 1
                if space[(b+1)%M][a] == standard :
                    space[(b+1%M)][a] = 'x'
                    space[b][a] = 'x'
                    count += 1


    #print(count)
    average = 0
    if count == 0:
        print(7777777777777777777777777777)
        sum1 = 0
        div = 0
        for b in range(1,N+1):
            for a in range(0,M):
                ele = space[b][a]
                if ele != 'x':
                    sum1 = sum1 + ele
                    div = div + 1

        average = sum1 / (div)

        print(sum1,div,average)


        for b in range(1,N+1):
            for a in range(0,M):
                value = space[b][a]
                if value != 'x':
                    if average > value:
                        space[b][a] += 1
                    elif average < value:
                        space[b][a] -= 1
        
    print(space)


# answer = 0
# for i in space:
#     answer = answer + sum(i)

# print(answer)
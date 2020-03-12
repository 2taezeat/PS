N, K = map(int,input().split())
nl = [i for i in range(2,N+1)]
l1 = [True for i in range(N+1)]
result = []
for i in range(2,N+1):
    if l1[i] == True:
        p = i
        l1[p] = False
        result.append(p)

    j = 1
    a = p*j

    while(a <= N):
        if l1[a] == True:
            l1[a] = False
            result.append(a)

        j = j + 1
        a = p * j

print(result[K-1])
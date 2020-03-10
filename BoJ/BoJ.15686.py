import itertools
import copy
N, M = map(int,input().split())
space = []
clist, hlist = [],[]

for i in range(N):
    a = list(map(int,input().split()))
    for s in range(N):
        if a[s] == 2:
            clist.append([i,s])
        if a[s] == 1:
            hlist.append([i,s])

    space.append(a)

c = list (map(tuple, itertools.combinations(clist, M) ) )
answer = []

for case in c:
    newclist = case
    result = []

    for y, x in hlist:
        dlist = []
        for cy,cx in newclist:
            d = abs(cy-y) + abs(cx-x)
            dlist.append(d)
        
        result.append(min(dlist))
    answer.append(sum(result))

print(min(answer))

import itertools
N, M = map(int,input().split())
space = []
clist, hlist = [],[] #clist는 치킨집이 있는 좌표를 나타냄, hlist는 집이 있는 좌표를 나타내는 리스트

for i in range(N):
    a = list(map(int,input().split()))
    for s in range(N):
        if a[s] == 2:
            clist.append([i,s])
        if a[s] == 1:
            hlist.append([i,s])

    space.append(a)

c = list (map(tuple, itertools.combinations(clist, M) ) ) # M개의 치킨집을 골라야 함으로.
answer = []

print(c)
for case in c:
    newclist = case
    result = []

    for y, x in hlist:
        dlist = []
        for cy,cx in newclist:
            d = abs(cy-y) + abs(cx-x)
            dlist.append(d)
        
        result.append(min(dlist))

    print(result)
    answer.append(sum(result))

print(min(answer))

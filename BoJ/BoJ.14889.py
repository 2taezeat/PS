import itertools
N = int(input())
space = []
for i in range(N):
    l1 = list(map(int,input().split()))
    space.append(l1)

tp = N // 2
pool = [i for i in range(N)]
a = list (map( list, itertools.combinations(pool, tp) ) ) 
len1 = len(a)
f = a[:len1//2]
l = a[len1//2:]
l.reverse()
result1 = []
result2 = []

for il in f:
    sum1 = 0
    ci = list (map( list, itertools.combinations(il, 2) ) )

    for i,j in ci:
        sum1 = sum1 + space[i][j] + space[j][i]

    result1.append(sum1)

for il in l:
    sum2 = 0
    ci = list (map( list, itertools.combinations(il, 2) ) )

    for i,j in ci:
        sum2 = sum2 + space[i][j] + space[j][i]

    result2.append(sum2)

answer = []
for i in range(len(result1)):
    answer.append(abs(result1[i]-result2[i]))

print(min(answer))
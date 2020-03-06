import itertools
N, M = map(int,input().split())
pool = [i for i in range(1,N+1)]
#a = list (map( tuple, itertools.permutations(pool, M) ) ) 
c = list (map( tuple, itertools.combinations(pool, M) ) ) 

for i in c:
    for k in i:
        print(k, end=' ')

    print()
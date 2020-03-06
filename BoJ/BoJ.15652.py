import itertools
N, M = map(int,input().split())
pool = [i for i in range(1,N+1)]
a = list (map( tuple, itertools.combinations_with_replacement(pool, M) ) )

for i in a:
    for k in i:
        print(k, end=' ')

    print()
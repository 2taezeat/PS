import itertools

n = int(input())
pool = []
for i in range(n):
    pool.append(i+1)

a = list(itertools.permutations(pool,n))

for i in a:
    for p in i:
        print(p, end= ' ')
    print()
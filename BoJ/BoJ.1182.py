import itertools
N, S = map(int,input().split())
A = list(map(int,input().split()))
answer = 0
for i in range(1,N+1):
    cl = list(map(list, itertools.combinations(A,i)))
    for l in cl:        
        if sum(l) == S:
            answer = answer + 1

print(answer)
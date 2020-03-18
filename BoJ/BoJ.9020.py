import itertools
T = int(input())
nl =[]
for i in range(T):
    nl.append(int(input()))
m = max(nl)
n = [True] * (m+1)
n[1] = n[0] = False
for i in range(2,m+1):
    if n[i] == True:
        p = i
    else:
        continue
    j = 2
    while(True):
        k = j * p
        j = j + 1
        if k > m:
            break
        n[k] = False 

prime = []
for i in range(2,m+1):
    if n[i] == True:
        prime.append(i)
comb = list(map(list,itertools.combinations_with_replacement(prime,2)))

for c in range(len(comb)):
    comb[c].append(comb[c][1]-comb[c][0])

comb.sort(key = lambda x: x[2])

for num in nl:
    for c in comb:
        if num == c[0] + c[1]:
            break
    
    print(c[0], c[1])
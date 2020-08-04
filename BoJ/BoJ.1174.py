import itertools
n = int(input())
l1 = ['9','8','7','6','5','4','3','2','1','0']
l2 = [] 

for i in range(1,11):
    a = list(map(''.join, itertools.combinations(l1, i)))
    for m in a:
        l2.append(m)
    
for i in range(len(l2)):
    l2[i] = int(l2[i])

l2.sort()

if n > 1023:
    print(-1)
else:
    print(l2[n-1])
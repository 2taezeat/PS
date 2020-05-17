n = int(input())
l2 = list(map(int,input().split()))

k = 0
for i in range(0,n-1):
    if l2[i] < l2[i+1]:
        k = i

m = 0
for i in range(k,n):
    if l2[k] < l2[i]:
        m = i

t1 = l2[m]
t2 = l2[k]
l2[m] = t2
l2[k] = t1

if k == 0 and m == 0:
    print(-1)
else:
    tl = l2[k+1:]
    tl.sort()
    l0 = l2[:k+1] + tl
    for num in l0:
        print(num, end= ' ')

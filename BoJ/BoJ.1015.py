n = int(input())
a = list(map(int,input().split()))
tl = []
a_ = [0]*n

for i in range(n):
    tl.append([a[i],i])

tl.sort()

for i in range(n):
    a_[i] = tl[i][1]

p = [0]*n


for i in range(n):
    p[a_[i]] = i

for i in p:
    print(i, end= ' ')
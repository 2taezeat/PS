n , x = map(int,input().split())
l = list(map(int,input().split()))
r = []
for i in l:
    if i < x:
        r.append(i)

for a in r:
    print(a, end= ' ')
N = int(input())
r = []
for i in range(N):
    a = int(input())
    r.append(a)

r.sort()
for i in range(N):
    print(r[i])
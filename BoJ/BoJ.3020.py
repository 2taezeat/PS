import bisect
import sys
input = sys.stdin.readline
N, H = map(int,input().split())
odd = []
even = []
for i in range(N):
    if i % 2 == 0:
        even.append(int(input()))
    else:
        odd.append(int(input()))

odd.sort()
even.sort()
r = []

for h in range(1,H+1):
    a = N//2 - bisect.bisect_left(even,h)
    r.append(a)

for g in range(1,H+1):
    rh = H-g+1
    b = N//2 - bisect.bisect_left(odd,rh)
    r[g-1] = r[g-1] + b

m = min(r)
c = 0
for i in r:
    if i == m:
        c += 1

print(m, c)
import sys
input = sys.stdin.readline
N = int(input())
wl, hl = [], []

for i in range(N):
    w, h = map(int,input().split())
    wl.append(w)
    hl.append(h)

rl = [1 for i in range(N)]
for i in range(N):

    for j in range(N):
        if i == j:
            continue
        else:
            if wl[i] < wl[j] and hl[i] < hl[j]:
                rl[i] = rl[i] + 1

for i in range(N):
    print(rl[i], end= ' ')
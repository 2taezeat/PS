import sys
from collections import deque
from itertools import permutations

def bomb(power, y, x):
    for ori in range(4):
        ny = y + dy[ori]
        nx = x + dx[ori]
        if 0 <= ny < W and 0 <= nx < H:
            Q.append((power - 1, ny, nx, ori))


def flame(fire, y, x, ori):
    ny = y + dy[ori]
    nx = x + dx[ori]
    if 0 <= ny < W and 0 <= nx < H:
        Q.append((fire - 1, ny, nx, ori))


# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,w,h = map(int,input().split())
    space = []
    for i in range(h):
        space.append(list(map(int,input().split())))

    l1 = [i for i in range(w)]
    print(l1)
    per = list(permutations(l1,n))

    print(per)

    for p in per:
       a,b,c = p[0],p[1],p[2]

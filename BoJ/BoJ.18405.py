from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int,input().split())
space,l1 = [],[]
for i in range(n):
    space.append(list(map(int,input().split())))
ts, tx, ty = map(int,input().split())
dx = [0, 1, 0, -1] #위, 오른쪽, 아래, 왼쪽
dy = [-1, 0, 1, 0]
l1 = [] # 바이러스에 대한 정보를 담는 리스트

def vcheck():
    for Y in range(n):
        for X in range(n):
            v = space[Y][X]
            if v != 0:
                l1.append((v,Y,X,0))
vcheck()
l1.sort()
q = deque(l1)


while q:
    vv,y,x,s = q.popleft()

    if ts == s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx > -1 and nx < n and ny > -1 and ny < n:
            if space[ny][nx] == 0:

                space[ny][nx] = vv
                q.append((vv,ny,nx,s+1))

print( space[tx-1][ty-1] )
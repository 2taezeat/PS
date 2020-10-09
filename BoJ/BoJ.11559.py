import sys
from collections import deque
space = []
for i in range(12):
    s = list(input())
    space.append(s)

print(space)


rl, yl, gl = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    q = deque()
    q.append([x,y])
    count = 1


while True:
    count = 0
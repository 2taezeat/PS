import sys
from collections import deque
import heapq
n = int(input())
space = []
for i in range(n):
    space.append(list(map(int,input().split())))



def bfs():
    pass


q = []
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            heapq.heappush(q, (y,x))

bfs()
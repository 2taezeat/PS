import sys
from collections import deque
N = int(sys.stdin.readline())
space = []
for i in range(N):
    space.append(list(map(int,sys.stdin.readline().split())))
answer = 0
dp = [[[0,0,0] for i in range(N)] for j in range(N)]
print(dp)
if space[-1][-1] == 1:
    print(0)
else:
    for i in range():
        for j in range():
            
            if space[i][j] == 0:
            dp[j][i][0] = dp[j][i][0] + 1




import sys
N = int(sys.stdin.readline())
space = []
for i in range(N):
    space.append(list(map(int,sys.stdin.readline().split())))
answer = 0
dp = [[[0,0,0] for i in range(N)] for j in range(N)]
dp[0][1][0] = 1
if space[-1][-1] == 1:
    print(0)
else:
    for i in range(0,N):
        for j in range(2,N):

            if space[i][j] == 1:
                dp[i][j][0] = 0
                dp[i][j][1] = 0
                dp[i][j][2] = 0

            elif space[i][j-1] == 1:
                dp[i][j][2] = dp[i-1][j][2] + dp[i-1][j][1]


            elif space[i-1][j] == 1:
                dp[i][j][0] =  dp[i][j-1][0] + dp[i][j-1][1]

            elif space[i-1][j-1] == 1:
                dp[i][j][0] = dp[i][j-1][0]
                dp[i][j][2] = dp[i-1][j][2]

            else:
                dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
                dp[i][j][1] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
                dp[i][j][2] = dp[i-1][j][2] + dp[i-1][j][1]

    print(sum(dp[-1][-1]))
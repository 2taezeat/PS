M, N = map(int,input().split())
space1 = []
for i in range(M):
    a = list(map(int,input().split()))
    space1.append(a)
dp = [ [-1] * N for _ in range(M)]
dp[0][0] = 1

def asd(Y,X,SPACE,DP):
    global M, N
    if DP[Y][X] >= 0:
        return

    DP[Y][X] = 0 
    if X > 0 and SPACE[Y][X-1] > SPACE[Y][X]:
        if DP[Y][X-1] == -1:
            asd(Y,X-1,SPACE,DP)
        DP[Y][X] = DP[Y][X] + DP[Y][X-1]

    if X < N - 1 and SPACE[Y][X+1] > SPACE[Y][X]:
        if DP[Y][X+1] == -1:
            asd(Y,X+1,SPACE,DP)
        DP[Y][X] = DP[Y][X] + DP[Y][X+1]

    if Y > 0 and SPACE[Y-1][X] > SPACE[Y][X]:
        if DP[Y-1][X] == -1:
            asd(Y-1,X,SPACE,DP)
        DP[Y][X] = DP[Y][X] + DP[Y-1][X]
        
    if Y < M - 1 and SPACE[Y+1][X] > SPACE[Y][X]:
        if DP[Y+1][X] == -1:
            asd(Y+1,X,SPACE,DP)
        DP[Y][X] = DP[Y][X] + DP[Y+1][X]


for i in range(M):
    for j in range(N):
        asd(i,j,space1,dp)

print(dp[M-1][N-1])
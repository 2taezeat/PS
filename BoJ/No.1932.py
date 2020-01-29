N = int(input())
dp1 = []

for i in range(N):
    array1 = list(map(int,input().split()))
    dp1.append(array1)

dp2 = [[0] * (N) for i in range(N-1)] # dp[N][K]
dp2.insert(0,dp1[0])


for i in range(1,N):
    for j in range(i+1):
        c = 0     
        if i == j :
            dp2[i][j] = dp2[i-1][j-1] + dp1[i][j]
            c = 1

        if j == 0 :
            dp2[i][j] = dp2[i-1][j] + dp1[i][j]
            c = 1

        if ( c == 0 ) :
            dp2[i][j] = max(dp2[i-1][j-1] + dp1[i][j], dp2[i-1][j] + dp1[i][j])

print(max(dp2[N-1]))
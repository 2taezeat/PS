N = int(input())
array2 = list(map(int,input().split()))
array2.insert(0,0)

dp = [[0] * (N + 1) for i in range(N + 1)] # dp[N][N]


for i in range(1,N+1):   
    for j in range(1,N+1):
        dp[i][j] = max( dp[i-1][j], dp[i-1][ j-array2[j] ] + array2[j] )
        dp[i][j] = max(array2[j], dp[i-]array2[j])
print(dp)

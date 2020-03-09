N, K = map(int,input().split())
dp = [ [1] * (N+1) for i in range(K)]
#DP[K][N] = K개를 더해서 합이 N일 경우의 수

for k in range(1,K):
    for n in range(N+1):
        sum1 = 0

        for l in range(n+1):
            sum1 = dp[k-1][n-l] + sum1
            
        dp[k][n] = sum1 % 1000000000
        
print(dp[-1][-1])
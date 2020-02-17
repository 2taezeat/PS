N = int(input())
array1 = [0]
for i in range(N):
    a = list(map(int,input().split()))
    array1.append(a)

dp = [ [0] * (3) for i in range(N+1)] # dp[i][c]

for i in range(1,N+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + array1[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + array1[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + array1[i][2]

print(min(dp[N]))
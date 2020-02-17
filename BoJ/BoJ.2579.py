N = int(input())
alist = [0,0,0]
for i in range(N):
    a = int(input())
    alist.append(a)

dp = [0 for i in range(N + 3)] 
for i in range(3, N+3):
    dp[i] = max( alist[i] + dp[i-2], alist[i] + alist[i-1] + dp[i-3] )

print(dp[-1])
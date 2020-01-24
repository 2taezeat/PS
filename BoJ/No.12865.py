N,K = map(int,input().split())

wlist = [0]
vlist = [0]

for i in range(N):
    w,v = map(int,input().split())
    wlist.append(w)
    vlist.append(v)

dp = [[0] * (K + 1) for i in range(N + 1)] # dp[N][K]

for i in range(1,N+1):
    
    for j in range(1,K+1):
        if j >= wlist[i]:
            dp[i][j] = max( dp[i-1][j], dp[i-1][ j-wlist[i] ] + vlist[i] )
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])            

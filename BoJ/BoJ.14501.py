# 0부터 시작 x , N부터 내려오기
N = int(input())
tlist = [0]
plist = [0]
for i in range(N):
    t, p = map(int,input().split())
    tlist.append(t)
    plist.append(p)

dp = [ 0 for i in range(N+2)]

for i in range(N,-1,-1):
    if i + tlist[i] > N+1:
        dp[i] = dp[i+1]

    else:
        dp[i] = max( plist[i] + dp[ i + tlist[i] ] , dp[i+1] )

print(dp[0])
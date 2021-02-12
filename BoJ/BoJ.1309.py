N = int(input())
dp = [3,7]
for i in range(2,N+1):
    a = ( dp[i-1]*2 + dp[i-2] ) % 9901
    dp.append( a )

print( dp[N-1] )
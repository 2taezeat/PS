N = int(input())
array2 = list(map(int,input().split()))
array2.insert(0,0)

dp = [-9999 for i in range(N + 1)] 

for i in range(1,N+1):   
    dp[i] = max( dp[i-1]+array2[i] , array2[i] )


print(max(dp))

N = int(input())
array1 = [0,0,0]
for i in range(N):
    a = int(input())
    array1.append(a)

dp = [0 for i in range(N + 3)] 

for i in range(3, N+3):
    dp[i] = max( dp[i-1], dp[i-2] + array1[i] , dp[i-3]+ array1[i] + array1[i-1] )

print(max(dp))
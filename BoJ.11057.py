n = int(input())
answer = []

dp = [ [1,1,1,1,1,1,1,1,1,1] ]

for i in range(1,n):
    l1 = []
    for j in range(0,10):

        sum1 = 0
        for k in range(0,j+1):
            sum1 = sum1 + dp[i-1][k]
        
        l1.append(sum1)

    dp.append(l1)


print(sum(dp[n-1]) % 10007)
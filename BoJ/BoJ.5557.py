N = int(input())
arr = list(map(int,input().split()))
key = arr[-1]
dp = [ [0]*21 for i in range(N-1)]
dp[0][arr[0]] = 1

for i in range(1,N-1):
    l1 = []
    for k in range(21):
        if dp[i-1][k] != 0:
            l1.append(k)

    for l in l1:
        if 0<= l-arr[i] <= 20:
            dp[i][ l-arr[i] ] = dp[i-1][ l ] + dp[i][ l-arr[i] ]

        if 0<= l+arr[i] <= 20:
            dp[i][ l+arr[i] ] = dp[i-1][ l ] + dp[i][ l+arr[i] ]


print(dp[-1][key])
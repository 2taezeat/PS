# DP_3_이태경.py

n = int(input())
l1 = list(map(int,input().split()))
# 최장 길이 부분수열 (LIS), 최장감소부분수열
dp = []
for i in range(n):
    dp.append(1)

for i in range(1,n):
    for j in range(0,i):

        if l1[i] < l1[j]: #        기존값
            dp[i] = max(dp[j] + 1, dp[i])


print(n - max(dp))
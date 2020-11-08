# DP_1_이태경.py
n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int,input().split())))
k = 2

# i는 열, j는 행
for i in range(1,n):
    for j in range(k):
        
        if j == 0: # 맨 왼쪽
            dp[i][j] = dp[i-1][j] + dp[i][j]

        elif i == j: # 맨 오른쪽
            dp[i][j] = dp[i][j] + dp[i-1][j-1]

        else: # 그 외 나머지, 중간에 있는 경우, # 왼쪽 위 값과 오른쪽 위 값 중 최대값
            dp[i][j] = dp[i][j] + max( dp[i-1][j] , dp[i-1][j-1] ) 
    
    k = k + 1

# 마지막 열에 있는 값중 최대값 출력
print( max(dp[n-1]) )

N ,M = map( int,  input().split() )
mlist = [0]+list(map(int, input().split()))
clist = [0]+list(map(int, input().split()))
c_sum = sum(clist)
dp = [[0] * (c_sum + 1) for i in range(N + 1)] # dp[N][M]
result = c_sum
# dp[i][j]는 i번째 앱까지 고려, 중 (j-cost)로 얻을 수 있는 최대의 byte를 의미한다.
# cost => 냅색 문제 가방 용량
for i in range(1,N+1):
    i_byte = mlist[i]
    i_cost = clist[i]

    for j in range(1,c_sum+1):
        if j >= i_cost:
            dp[i][j] = max( dp[i-1][j], dp[i-1][ j-i_cost ] + i_byte )
        else:
            dp[i][j] = dp[i-1][j]

        if dp[i][j] >= M: 
            result = min(result, j)

print(result) 
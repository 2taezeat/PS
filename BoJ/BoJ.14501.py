# DP_2_이태경.py

N = int(input())
tlist = [0] # 걸리는 기간 tlist
plist = [0] # 받을 수 있는 금액 plist
for i in range(N):
    t, p = map(int,input().split())
    tlist.append(t)
    plist.append(p)

# 뒤부터 시작
# i번째 날부터 ~ 마지막 날(N)까지 낼 수 있는 최대 이윤은
# 1. 현재 일의 이윤 + 현재 일이 필요한 day 뒤의 이윤
# 2. 현재 일을 하지 않고 넘어갈 때의 이윤 (i+1의 이윤)
# 1.2.중 최대값.
dp = [ 0 for i in range(N+2)]
print(dp)

for i in range(N,-1,-1):
    print(i)
    # i번째 날에 걸리는 시간이 N+1을 넘기면, 상담 불가능 
    if i + tlist[i] > N+1:
        dp[i] = dp[i+1]

    else:
        dp[i] = max( plist[i] + dp[ i + tlist[i] ] , dp[i+1] )

print(dp)
print(dp[0])
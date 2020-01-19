N = int(input())
a = []
b = list(map(int, input().split()))

for j in range(N):
    a.append(b[j])

dp = [1]

for k in range(1,N):
    count = 0
    clist = [0]
    maxdp = dp[0]

    for j in range(k):
        if a[k] > a[j] :
            clist.append(j)

    if clist == [0]:
        dp.append(maxdp)
    else:
        for c in clist:
            if dp[c] > maxdp:
                maxdp = dp[c]

        dp.append(maxdp + 1)        

print(max(dp))
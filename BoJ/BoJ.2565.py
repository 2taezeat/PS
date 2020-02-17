N = int(input())
l1 = []
for i in range(N):
    a,b = map(int,input().split())
    l1.append([a,b])
l1.sort()
bl = [ i[1] for i in l1]
dp = [1]

for i in range(1,N):
    maxdp = 1
    c_l = []
    for j in range(i):
        if bl[i] > bl [j]:
            c_l.append(j)
    
    if c_l == []: # count되는것이 없으면
        dp.append(maxdp)
    else:
        for c in c_l:
            if maxdp < dp[c]:
                maxdp = dp[c]

        dp.append(maxdp + 1)

print(N-max(dp))
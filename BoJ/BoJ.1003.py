T = int(input())
nlist = []
for i in range(T):
    N = int(input())
    nlist.append(N)

maxN = max(nlist)
dp0 = []
dp1 = []

for j in range(maxN+1):
    if j == 0 :
        dp0.append(1)
        dp1.append(0)
    elif j == 1:
        dp0.append(0)
        dp1.append(1)
    elif j == 2:
        dp0.append(1)
        dp1.append(1)
    else:
        dp0.append( dp0[j-1] + dp0[j-2])
        dp1.append( dp1[j-1] + dp1[j-2])

for k in nlist:
    print(dp0[k], dp1[k])
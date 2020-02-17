N = int(input())
list1 = list(map(int, input().split()))
dp1 = [0 for i in range(N-1)]
dp1.insert(0,1)
dp2 = [0 for i in range(N-1)]
dp2.insert(0,1)
list2 = list(reversed(list1))

for i in range(1,N):
    countlist = [0 for m in range(N)]
    countlist2 = [0 for n in range(N)]

    for k in range(i):
        if list1[k] < list1[i]:
            countlist[k] = 1

        if list2[k] < list2[i]:
            countlist2[k] = 1
    c = 0
    maxdp = dp1[0]
    d = 0
    maxdp2 = dp2[0]


    for j in range(N):
        if (countlist[j] == 1):
            c = 1
            if maxdp < dp1[j]:
                maxdp = dp1[j]
    #####################################
        if (countlist2[j] == 1):
            d = 1
            if maxdp2 < dp2[j]:
                maxdp2 = dp2[j]
        
    if c == 0:
        dp1[i] = maxdp
    else:
        dp1[i] = maxdp + 1

#####################################
    if d == 0:
        dp2[i] = maxdp2
    else:
        dp2[i] = maxdp2 + 1


ndp2 = list(reversed(dp2))
a = []
for i in range(N):
    a.append(dp1[i] + ndp2[i])

print(max(a)-1)

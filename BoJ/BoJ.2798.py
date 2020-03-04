import sys
input = sys.stdin.readline
N, M = map(int,input().split())
cardlist = list(map(int,input().split()))
cardlist.sort()
a = cardlist[-1] + cardlist[-2] + cardlist[-3]

if a <= M:
    result = a
else: 
    l = len(cardlist)
    q = 0
    result = 0
    for i in range(l):
        sum1 = 0
        if q == 3:
            break
        for j in range(i+1,l):
            if q == 3:
                break
            for k in range(j+1,l):
                sum1 = cardlist[i] + cardlist[j] + cardlist[k]
                if sum1 == M:
                    result = sum1
                    q = 3
                    break
                elif sum1 < M:
                    if sum1 > result:
                        result = sum1


print(result)
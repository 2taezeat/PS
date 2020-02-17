from math import floor
N = int(input())
A,B = map(int,input().split())
C = int(input())

D = []
for k in range(N):
    k = int(input())
    D.append(k)

D.sort(reverse=True)
#####

firstrate = C/A

DR = []
for i in range(N):
    drate = D[i] / B
    DR.append(drate)

for j in range(N):
    if DR[j] > firstrate:
        firstrate =  (sum(D[0:j+1]) + C) / (A + B*(j+1))
    else:
        break

print(floor(firstrate))
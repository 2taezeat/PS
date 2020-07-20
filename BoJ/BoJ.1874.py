import sys
input = sys.stdin.readline
n = int(input())
l1,ml,pl = [],[],[]
c = 0
for i in range(n):
    l1.append(int(input()))
l1.sort()
mid = l1[n//2]
for i in range(-8000,8001,1):
    ml.append(0)


for i in range(n):
    ml[l1[i]+8000] = ml[l1[i]+8000] + 1
maml = max(ml)

for j in range(len(ml)):
    if ml[j] == maml:
        c = c + 1
        pl.append( [ j-8000, ml[j] ] )
    
    if c == 2:
        break

if c >= 2:
    most = pl[1][0]
else:
    most = ml.index(maml) - 8000

aver = sum(l1) / n
rang = l1[-1] - l1[0]
print(int(round(aver,0)))
print(mid)
print(most)
print(rang)
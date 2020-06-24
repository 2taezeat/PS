import sys
input = sys.stdin.readline

n = int(input())

l0 = []
for i in range(n):
    l1 = input().strip().split()
    d0 = {'name':l1[0],'rnr':int(l1[1]),'dud':int(l1[2]),'tn':int(l1[3]), }

    l0.append(d0)

newl0 = sorted(l0, key = lambda x :( -x['rnr'], x['dud'], -x['tn'], x['name']  ) )

for i in newl0:
    print(i['name'])
import sys
 
input = sys.stdin.readline
n = int(input())
s0 = set()
l0 = []
for i in range(n):
    l1 = list(map(str,input().split()))

    s0.add(l1[0])
    l0.append(l1)

l_s0 = list(s0)
d0 = {}
for i in l_s0:
    d0[i] = 0

for i in range(n):
    if l0[i][1] == 'enter':
        d0[ l0[i][0] ] = d0[ l0[i][0] ] + 1 
    else:
        d0[ l0[i][0] ] = d0[ l0[i][0] ] - 1

al = []
for n,c in d0.items():
    if c == 1:
        al.append([n,c])

al.sort(reverse=True)
for i in range(len(al)):
    print(al[i][0])